# Generated by Django 5.0 on 2024-01-09 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=200),
        ),
    ]