# Generated by Django 5.0.4 on 2024-05-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0005_remove_resumebuilder_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumebuilder',
            name='linkedin',
            field=models.URLField(default='http://www.linkedin.com/default', null=True),
        ),
    ]
