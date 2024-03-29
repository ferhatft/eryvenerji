# Generated by Django 4.1.7 on 2023-02-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iletisim", "0006_contact_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="il",
            field=models.CharField(
                max_length=150, null=True, verbose_name="sistemin kurulacağı il"
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="location",
            field=models.CharField(
                max_length=150, null=True, verbose_name="sistemin kurulacağı yer"
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="system",
            field=models.CharField(
                max_length=150, null=True, verbose_name="talep ettiğiniz sistem"
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=30, verbose_name="tam isim"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="telefon"
            ),
        ),
    ]
