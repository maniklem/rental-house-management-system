# Generated by Django 4.0.2 on 2022-02-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0025_rename_weeks_consuption_waterconsumption_weeks_consumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='water',
            name='unit',
            field=models.CharField(default='Litres', max_length=20),
        ),
    ]
