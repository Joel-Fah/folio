# Generated by Django 5.0 on 2024-01-09 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_project_tinymce_content_alter_project_ended_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tinymce_content',
            new_name='content',
        ),
    ]
