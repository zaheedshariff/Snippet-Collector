# Generated by Django 3.1.1 on 2020-11-16 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0011_auto_20201116_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usagecounter',
            old_name='project_type',
            new_name='type',
        ),
    ]
