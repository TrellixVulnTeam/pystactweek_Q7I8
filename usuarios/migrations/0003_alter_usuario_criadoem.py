# Generated by Django 3.2.8 on 2021-10-09 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_criadoem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='criadoem',
            field=models.DateField(default=datetime.datetime(2021, 10, 9, 14, 55, 1, 253534)),
        ),
    ]
