# Generated by Django 4.0.2 on 2022-03-20 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities_and_rent', '0095_mpesapayent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MpesaPayent',
            new_name='MpesaPayment',
        ),
    ]
