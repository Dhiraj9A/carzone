# Generated by Django 4.1.1 on 2023-04-05 07:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='desctiption',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(),
        ),
    ]
