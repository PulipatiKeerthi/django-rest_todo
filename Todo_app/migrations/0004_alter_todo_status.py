# Generated by Django 4.2.1 on 2023-05-31 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_app', '0003_tag_todo_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='open', max_length=20),
        ),
    ]
