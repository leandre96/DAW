# Generated by Django 2.0.7 on 2018-07-30 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('servicio', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(verbose_name='fecha en la que adquirio el servicio')),
            ],
        ),
    ]