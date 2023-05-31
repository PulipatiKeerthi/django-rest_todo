# Generated by Django 4.2.1 on 2023-05-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=1000)),
                ('Time_stamp', models.DateTimeField(auto_now=True)),
                ('Due_date', models.DateTimeField()),
            ],
        ),
    ]