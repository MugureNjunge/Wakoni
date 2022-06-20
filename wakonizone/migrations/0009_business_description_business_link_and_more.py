# Generated by Django 4.0.5 on 2022-06-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wakonizone', '0008_rename_business_name_business_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='business',
            name='link',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]