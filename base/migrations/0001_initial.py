# Generated by Django 4.1.7 on 2023-03-24 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('serviceType', models.TextField()),
                ('orderid', models.TextField()),
                ('redirectUrl', models.TextField()),
                ('iat', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('lang', models.TextField()),
            ],
        ),
    ]
