# Generated by Django 2.1.7 on 2019-04-03 14:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_ide', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('message', models.TextField(blank=True)),
                ('dated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
