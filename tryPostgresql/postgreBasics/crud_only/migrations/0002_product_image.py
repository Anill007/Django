# Generated by Django 3.1 on 2020-08-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_only', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(default='try1.png', upload_to='media_forms'),
        ),
    ]
