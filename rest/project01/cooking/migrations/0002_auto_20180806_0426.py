# Generated by Django 2.0.7 on 2018-08-06 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha',
            field=models.DateField(verbose_name='fecha en la que adquirio el servicio'),
        ),
    ]
