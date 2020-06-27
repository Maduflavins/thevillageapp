# Generated by Django 3.0 on 2020-06-23 14:46

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0006_booking_space'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='isavailable',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='space',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='villager',
        ),
        migrations.AddField(
            model_name='booking',
            name='villager_fname',
            field=models.CharField(default='first_fname', max_length=150),
        ),
        migrations.AddField(
            model_name='booking',
            name='villager_lname',
            field=models.CharField(default='last_name', max_length=150),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='email@email.com', max_length=250),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='booking',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plans.Plan'),
        ),
        migrations.DeleteModel(
            name='Space',
        ),
    ]