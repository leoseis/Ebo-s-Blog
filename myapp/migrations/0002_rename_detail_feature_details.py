# Generated by Django 4.2.4 on 2023-11-15 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='detail',
            new_name='details',
        ),
    ]
