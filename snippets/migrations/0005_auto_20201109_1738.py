# Generated by Django 3.1.1 on 2020-11-09 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20201109_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='year_entered',
            new_name='year_discovered',
        ),
    ]
