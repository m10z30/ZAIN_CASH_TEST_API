# Generated by Django 4.1.7 on 2023-03-24 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_account_rename_number_merchant_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='operation_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
