# Generated by Django 4.0.5 on 2022-06-30 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_rename_applybuttonlink_program_apply_button_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='program_snapshot',
            new_name='description_short',
        ),
    ]