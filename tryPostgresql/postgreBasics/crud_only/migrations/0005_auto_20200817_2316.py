# Generated by Django 3.1 on 2020-08-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_only', '0004_auto_20200817_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.FileField(upload_to='one/'),
        ),
    ]
