# Generated by Django 5.0.1 on 2024-01-23 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='tags',
        ),
    ]
