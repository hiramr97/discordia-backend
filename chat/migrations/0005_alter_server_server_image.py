# Generated by Django 4.1.5 on 2023-01-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='server_image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
