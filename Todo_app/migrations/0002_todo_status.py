# Generated by Django 4.2.1 on 2023-05-31 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
    ]
