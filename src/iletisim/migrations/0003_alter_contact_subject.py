# Generated by Django 3.2.4 on 2021-06-09 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0002_auto_20210609_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('teklif almak istiyorum', 'Teklif almak istiyorum'), ('bilgi almak istiyorum ', 'Bilgi almak istiyorum '), ('tanışma toplantısı talep ediyorum ', 'Tanışma toplantısı talep ediyorum ')], default='teklif almak istiyorum', max_length=500),
        ),
    ]
