# Generated by Django 4.1.7 on 2023-02-26 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0010_remove_portfoliomodel_category_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="portfoliomodelgaleri",
            options={
                "ordering": ["created_date"],
                "verbose_name": "Resim",
                "verbose_name_plural": "Resimler",
            },
        ),
        migrations.AlterField(
            model_name="portfoliomodelgaleri",
            name="image",
            field=models.ImageField(upload_to="portfolio/", verbose_name="resim"),
        ),
        migrations.CreateModel(
            name="ProjelerimizModelGaleri",
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
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="projeler/", verbose_name="resim"),
                ),
                (
                    "proje",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ProjelerimizModelGaleri",
                        to="portfolio.projelerimiz",
                    ),
                ),
            ],
            options={
                "verbose_name": "Resim",
                "verbose_name_plural": "Resimler",
                "ordering": ["created_date"],
            },
        ),
    ]
