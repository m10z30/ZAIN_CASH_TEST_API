# Generated by Django 4.1.7 on 2023-03-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_orderid_transaction_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]