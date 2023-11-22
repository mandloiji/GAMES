# Generated by Django 4.2.2 on 2023-08-23 13:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='tech',
            name='heading',
            field=tinymce.models.HTMLField(),
        ),
    ]