# Generated by Django 3.2.4 on 2022-03-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20220306_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodel',
            name='creator',
            field=models.CharField(blank=True, max_length=40, verbose_name='créateur'),
        ),
    ]