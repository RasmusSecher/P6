# Generated by Django 4.0.4 on 2022-05-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_attribute_name_alter_attribute_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='executionTime',
            field=models.TextField(default=''),
        ),
    ]
