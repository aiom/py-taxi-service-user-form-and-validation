# Generated by Django 4.1 on 2024-01-31 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]{3}[0-9]{6}$', 'Only')]),
        ),
    ]