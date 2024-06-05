# Generated by Django 5.0.2 on 2024-03-27 09:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_medicine_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
        ),
    ]
