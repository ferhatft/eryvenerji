# Generated by Django 4.1.7 on 2023-02-26 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("haber", "0017_auto_20220320_1618"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogmodel",
            options={
                "ordering": ["created_date"],
                "verbose_name": "Haber",
                "verbose_name_plural": "Haberler",
            },
        ),
        migrations.RemoveField(
            model_name="blogmodel",
            name="rating",
        ),
        migrations.RemoveField(
            model_name="blogmodel",
            name="slug",
        ),
        migrations.AlterField(
            model_name="blogmodel",
            name="category",
            field=models.CharField(blank=True, max_length=40, verbose_name="kategori"),
        ),
        migrations.AlterField(
            model_name="blogmodel",
            name="created_date",
            field=models.DateField(
                auto_now_add=True, null=True, verbose_name="oluşturulma tarihi"
            ),
        ),
        migrations.AlterField(
            model_name="blogmodel",
            name="image",
            field=models.ImageField(null=True, upload_to="", verbose_name="resim"),
        ),
    ]
