# Generated by Django 3.1 on 2021-05-22 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_config', '0003_auto_20210519_0329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelconfig',
            options={'ordering': ['name'], 'verbose_name': 'model config', 'verbose_name_plural': 'model configs'},
        ),
    ]