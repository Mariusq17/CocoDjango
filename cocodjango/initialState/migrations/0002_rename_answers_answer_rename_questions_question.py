# Generated by Django 5.1.6 on 2025-03-21 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('initialState', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
