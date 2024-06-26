# Generated by Django 5.0.6 on 2024-06-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoilo', '0006_remove_contact_phone_contact_linkedin_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='resume_link',
        ),
        migrations.AddField(
            model_name='contact',
            name='resume',
            field=models.FileField(default='https://example.com/resume.pdf', upload_to='resumes/'),
            preserve_default=False,
        ),
    ]
