# Generated by Django 4.2 on 2023-05-04 10:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_cars_car_photo_alter_cars_car_photo1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
