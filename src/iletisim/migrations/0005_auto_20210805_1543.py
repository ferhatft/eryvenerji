# Generated by Django 3.2.4 on 2021-08-05 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0004_newsletter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsletter',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]
