# Generated by Django 4.0.2 on 2022-07-21 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_dates_delete_mymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dates',
            name='date',
        ),
    ]