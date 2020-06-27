# Generated by Django 3.0 on 2020-06-23 21:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0009_auto_20200623_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='villager_fname',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='villager_lname',
        ),
        migrations.AddField(
            model_name='booking',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='booking',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='dateBooked',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message='must be a valid phone number', regex='^\\+[0-9]{1,3}\\.[0-9]{4,14}(?:x.+)?$')]),
        ),
    ]