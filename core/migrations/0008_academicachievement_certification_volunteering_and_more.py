# Generated by Django 5.0 on 2024-01-12 08:33

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_project_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('date_earned', models.DateField()),
                ('institution', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True, null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('date_earned', models.DateField()),
                ('organisation', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='achievements/certifications/')),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('organisation', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='achievements/volunteering/')),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]