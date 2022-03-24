# Generated by Django 4.0.2 on 2022-03-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0013_remove_rentdefaulters_parent_defaults_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rentdefaulters',
            options={'verbose_name': 'Rent Defaulters', 'verbose_name_plural': 'Rent Defaulters'},
        ),
        migrations.RemoveField(
            model_name='unitrentdetails',
            name='linked_to_defaulters',
        ),
        migrations.AlterField(
            model_name='unitrentdetails',
            name='status',
            field=models.CharField(choices=[('refunded', 'Refunded'), ('open', 'open'), ('closed', 'closed'), ('defaulted', 'Added To Defaulted')], default='open', max_length=15),
        ),
    ]
