# Generated by Django 3.2.8 on 2021-10-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apples_types', '0003_apples_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apples',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/%y/%m/%d'),
        ),
    ]
