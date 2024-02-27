# Generated by Django 4.1.7 on 2023-02-26 01:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0009_projelerimiz_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="portfoliomodel",
            name="category",
        ),
        migrations.RemoveField(
            model_name="portfoliomodel",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="portfoliomodel",
            name="mainimage",
        ),
        migrations.RemoveField(
            model_name="portfoliomodel",
            name="rating",
        ),
        migrations.RemoveField(
            model_name="portfoliomodel",
            name="slug",
        ),
        migrations.AlterField(
            model_name="portfoliomodel",
            name="decription",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True, verbose_name="açıklama"
            ),
        ),
        migrations.AlterField(
            model_name="portfoliomodel",
            name="title",
            field=models.CharField(blank=True, max_length=40, verbose_name="başlık"),
        ),
    ]
