# Generated by Django 5.0.4 on 2024-04-16 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='department',
        ),
    ]
