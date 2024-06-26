# Generated by Django 5.0.4 on 2024-05-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_technologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='appStoreUrl',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='descriptionEN',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='descriptionSP',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='portfolio/images/covers'),
        ),
        migrations.AlterField(
            model_name='project',
            name='playStoreUrl',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='repositoryUrl',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='screen1',
            field=models.ImageField(blank=True, default=None, upload_to='portfolio/images/screens'),
        ),
        migrations.AlterField(
            model_name='project',
            name='screen2',
            field=models.ImageField(blank=True, default=None, upload_to='portfolio/images/screens'),
        ),
        migrations.AlterField(
            model_name='project',
            name='screen3',
            field=models.ImageField(blank=True, default=None, upload_to='portfolio/images/screens'),
        ),
    ]
