# Generated by Django 4.0.5 on 2022-06-20 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wakonizone', '0005_remove_profile_fullname_remove_profile_locality_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='hood',
            new_name='locality',
        ),
    ]
