# Generated by Django 4.0.2 on 2022-03-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0072_alter_electricitybilling_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electricitybilling',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='waterbilling',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
