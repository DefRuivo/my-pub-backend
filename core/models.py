import random
import string

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("E-mail"), unique=True, help_text=_("E-mail do usuário")
    )
    first_name = models.CharField(
        _("Nome"), max_length=30, blank=True, help_text=_("Primeiro nome")
    )
    last_name = models.CharField(
        _("Sobrenome"), max_length=30, blank=True, help_text=_("Nome de família")
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = models.BooleanField(
        _("Usuário ativo?"),
        default=True,
        help_text=_("Indica se o usuário está ativo ou não"),
    )
    is_staff = models.BooleanField(
        _("Equipe?"), default=True, help_text=_("Faz parte da equipe da loja?")
    )
    is_superuser = models.BooleanField(
        _("Adminstrador?"), default=False, help_text=_("É um administrador do sistema?")
    )
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    WRITE_FIELDS = [
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    ]

    class Meta:
        ordering = ["first_name", "last_name", "email"]
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name or "Sem"

    @property
    def get_abbrv(self):
        try:
            return f"{self.first_name[0]}{self.last_name[0]}"
        except IndexError:
            return "SN"

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def roles(self):
        roles = []
        if self.is_staff:
            roles.append("STAFF")

        if self.is_superuser:
            roles.append("ADMIN")

        return roles

    @property
    def serialize(self):
        return {
            "id": self.pk,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_joined": self.date_joined,
            "active": self.is_active,
            "name": self.get_full_name(),
            "short_name": self.get_short_name(),
            "abbrv": self.get_abbrv,
            "roles": self.roles,
        }


class Brand(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField("Nome", max_length=191, help_text="Nome da marca")
    website = models.URLField("Website", null=True, blank=True)
    facebook = models.URLField("Facebook", null=True, blank=True)
    twitter = models.URLField("Twitter", null=True, blank=True)
    linkedin = models.URLField("LinkedIn", null=True, blank=True)

    def __str__(self):
        return self.name


class VolumeChoices(models.TextChoices):
    KG = "Kg"
    L = "L"
    U = "Unidade"


class ProductCategoryChoices(models.TextChoices):
    PERSONAL_HYGIENE = "Higiene Pessoal"
    FOOD = "Alimento"
    CLEANING = "Limpeza"
    OTHER = "Outro"


def get_product_image_upload_path(instance, filename):
    extension = filename.split(".")[-1].lower()
    return f"products/{instance.pk}.{extension}"


class Product(models.Model):
    brand = models.ForeignKey("core.Brand", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        "Imagem principal",
        upload_to=get_product_image_upload_path,
        max_length=191,
        null=True,
        blank=True,
        help_text="Imagem principal do produto",
        default="no-image.png",
    )
    category = models.CharField(
        "Categoria do produto",
        help_text="Informe corretamente a categoria do produto para não ter supresas",
        db_index=True,
        max_length=20,
        choices=ProductCategoryChoices.choices,
        default=ProductCategoryChoices.OTHER,
    )
    name = models.CharField(
        "Nome",
        help_text="Nome do produto",
        max_length=191,
    )
    barcode = models.CharField(
        "Código de barras",
        db_index=True,
        max_length=191,
        blank=True,
        null=True,
    )
    description = models.TextField(
        "Descrição",
        max_length=5000,
        help_text="Descrição do produto",
        null=True,
        blank=True,
    )
    quantity = models.FloatField(
        "Quantidade",
        help_text="Quantidade do produto na embalagem",
        blank=True,
        null=True,
    )
    quantity_unit = models.CharField(
        "Unidade da quantidade",
        help_text="Unidade utilizada para medir a quantidade do produto na embalagem",
        max_length=20,
        choices=VolumeChoices.choices,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.brand} {self.name} ({self.quantity}{self.quantity_unit})"


class ProductItem(models.Model):
    product = models.ForeignKey("core.Product", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField("Quantidade", help_text="Quantidade disponível")
    bought_in = models.DateField(
        "Data de compra",
        blank=True,
        null=True,
        help_text="Data de compra do item",
    )
    valid_until = models.DateField(
        "Válido até",
        blank=True,
        null=True,
        help_text="Data de validade",
    )
    batch = models.CharField(
        "Lote",
        max_length=191,
        blank=True,
        null=True,
        help_text="Lote do produto",
    )

    def __str__(self):

        return self.product
