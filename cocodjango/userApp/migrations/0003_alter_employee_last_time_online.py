# Generated by Django 5.1.6 on 2025-03-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_alter_employee_my_buddy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='last_time_online',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
