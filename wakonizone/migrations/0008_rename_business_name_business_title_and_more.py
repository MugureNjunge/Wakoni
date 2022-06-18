# Generated by Django 4.0.5 on 2022-06-18 19:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wakonizone', '0007_business'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='locality_image',
        ),
        migrations.AddField(
            model_name='business',
            name='business_image',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
