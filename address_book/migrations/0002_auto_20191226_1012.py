# Generated by Django 2.1 on 2019-12-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
    ]
