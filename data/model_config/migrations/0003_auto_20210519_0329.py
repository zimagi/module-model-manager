# Generated by Django 3.1 on 2021-05-19 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_config', '0002_modelconfig_hyperparameters'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelconfig',
            options={'ordering': ['name'], 'verbose_name': 'config', 'verbose_name_plural': 'configs'},
        ),
    ]