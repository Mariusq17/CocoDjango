# Generated by Django 5.1.6 on 2025-03-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0004_alter_employee_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(blank=True, default=2000, null=True),
        ),
    ]
