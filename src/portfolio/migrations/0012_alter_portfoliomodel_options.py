# Generated by Django 4.1.7 on 2023-02-26 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0011_alter_portfoliomodelgaleri_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="portfoliomodel",
            options={
                "ordering": ["id"],
                "verbose_name": "Ürün",
                "verbose_name_plural": "Ürünler",
            },
        ),
    ]
