# Generated by Django 4.0.2 on 2022-03-02 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0035_waterbilling_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterbilling',
            name='added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
