# Generated by Django 5.0.6 on 2024-06-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoilo', '0002_remove_contact_address_alter_project_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateField(),
        ),
    ]
