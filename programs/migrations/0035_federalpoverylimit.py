# Generated by Django 4.0.5 on 2023-05-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0034_alter_urgentneedtranslation_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='FederalPoveryLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=32)),
                ('has_1_person', models.IntegerField()),
                ('has_2_person', models.IntegerField()),
                ('has_3_person', models.IntegerField()),
                ('has_4_person', models.IntegerField()),
                ('has_5_person', models.IntegerField()),
                ('has_6_person', models.IntegerField()),
                ('has_7_person', models.IntegerField()),
                ('has_8_person', models.IntegerField()),
            ],
        ),
    ]
