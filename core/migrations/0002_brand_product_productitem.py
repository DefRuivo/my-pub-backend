# Generated by Django 3.2 on 2021-05-01 20:40

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Nome da marca", max_length=191, verbose_name="Nome"
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="Website"),
                ),
                (
                    "facebook",
                    models.URLField(blank=True, null=True, verbose_name="Facebook"),
                ),
                (
                    "twitter",
                    models.URLField(blank=True, null=True, verbose_name="Twitter"),
                ),
                (
                    "linkedin",
                    models.URLField(blank=True, null=True, verbose_name="LinkedIn"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="no-image.png",
                        help_text="Imagem principal do produto",
                        max_length=191,
                        null=True,
                        upload_to=core.models.get_product_image_upload_path,
                        verbose_name="Imagem principal",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Higiene Pessoal", "Personal Hygiene"),
                            ("Alimento", "Food"),
                            ("Limpeza", "Cleaning"),
                            ("Outro", "Other"),
                        ],
                        db_index=True,
                        default="Outro",
                        max_length=20,
                        verbose_name="Categoria do produto",
                        help_text="Informe corretamente a categoria do produto para não ter supresas",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Nome do produto", max_length=191, verbose_name="Nome"
                    ),
                ),
                (
                    "barcode",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=191,
                        null=True,
                        verbose_name="Código de barras",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Descrição do produto",
                        max_length=5000,
                        verbose_name="Descrição",
                    ),
                ),
                (
                    "quantity",
                    models.FloatField(
                        blank=True,
                        help_text="Quantidade do produto na embalagem",
                        null=True,
                        verbose_name="Quantidade",
                    ),
                ),
                (
                    "quantity_unit",
                    models.CharField(
                        blank=True,
                        choices=[("Kg", "Kg"), ("L", "L"), ("Unidade", "U")],
                        max_length=20,
                        null=True,
                        verbose_name="Unidade da quantidade",
                        help_text="Unidade utilizada para medir a quantidade do produto na embalagem",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.brand"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "quantity",
                    models.IntegerField(
                        help_text="Quantidade disponível", verbose_name="Quantidade"
                    ),
                ),
                (
                    "bought_in",
                    models.DateField(
                        blank=True,
                        help_text="Data de compra do item",
                        null=True,
                        verbose_name="Data de compra",
                    ),
                ),
                (
                    "valid_until",
                    models.DateField(
                        blank=True,
                        help_text="Data de validade",
                        null=True,
                        verbose_name="Válido até",
                    ),
                ),
                (
                    "batch",
                    models.CharField(
                        blank=True,
                        help_text="Lote do produto",
                        max_length=191,
                        null=True,
                        verbose_name="Lote",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.product"
                    ),
                ),
            ],
        ),
    ]