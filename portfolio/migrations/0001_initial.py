# Generated by Django 5.0.4 on 2024-05-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('playStoreUrl', models.CharField(default=None, max_length=255)),
                ('appStoreUrl', models.CharField(default=None, max_length=255)),
                ('repositoryUrl', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]