# Generated by Django 3.1 on 2020-08-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_only', '0003_auto_20200817_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.FileField(default='try1.png', upload_to='one'),
        ),
    ]
