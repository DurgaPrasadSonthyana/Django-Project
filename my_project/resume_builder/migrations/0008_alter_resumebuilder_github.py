# Generated by Django 5.0.4 on 2024-05-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0007_resumebuilder_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumebuilder',
            name='github',
            field=models.URLField(blank=True, default='gihub', null=True),
        ),
    ]
