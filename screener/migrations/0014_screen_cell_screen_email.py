# Generated by Django 4.0.5 on 2022-08-10 00:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('screener', '0013_householdmember_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='cell',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='screen',
            name='email',
            field=models.CharField(blank=True, max_length=320),
        ),
    ]