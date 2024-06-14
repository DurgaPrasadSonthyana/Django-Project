# Generated by Django 5.0.4 on 2024-05-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0002_resumebuilder_delete_resume_builder'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumebuilder',
            name='address',
            field=models.CharField(default='Hyderabad, Telangana', max_length=255),
        ),
        migrations.AddField(
            model_name='resumebuilder',
            name='email',
            field=models.EmailField(default='durga@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='resumebuilder',
            name='github',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='resumebuilder',
            name='linkedin',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='resumebuilder',
            name='name',
            field=models.CharField(default='Enter Name', max_length=100),
        ),
        migrations.AddField(
            model_name='resumebuilder',
            name='number',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='resumebuilder',
            name='title',
            field=models.CharField(default='None', max_length=75),
        ),
    ]
