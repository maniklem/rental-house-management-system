# Generated by Django 4.0.2 on 2022-03-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0017_payonlinempesa_receipt_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payonlinempesa',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
