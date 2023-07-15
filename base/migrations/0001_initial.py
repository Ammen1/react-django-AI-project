# Generated by Django 4.0.1 on 2023-07-09 08:19

import base.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=255)),
                ('severity', models.IntegerField()),
                ('original_image', models.ImageField(upload_to=base.models.original_image)),
                ('detected_image', models.ImageField(upload_to=base.models.detected_image)),
                ('segmented_image', models.ImageField(upload_to=base.models.segmented_image)),
                ('locations', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ('-detected_image',),
            },
        ),
    ]
