# Generated by Django 4.0.2 on 2022-03-20 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0093_mpesapayments_confirmed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MpesaPayments',
        ),
    ]
