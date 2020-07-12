# Generated by Django 3.0 on 2020-07-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0018_auto_20200707_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='renewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan_img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
