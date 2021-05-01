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
