# Generated by Django 2.1.7 on 2019-03-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='email',
            field=models.EmailField(default='none@none.com', max_length=254),
        ),
    ]