# Generated by Django 2.1.7 on 2019-03-14 13:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('sqft', models.IntegerField()),
                ('photommain', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('published', models.BooleanField(default=True)),
                ('dated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]
