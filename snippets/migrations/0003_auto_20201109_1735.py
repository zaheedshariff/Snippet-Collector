# Generated by Django 3.1.1 on 2020-11-09 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20201109_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='breed',
            new_name='lanaguage',
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='age',
            new_name='year_discovered',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='name',
        ),
        migrations.AddField(
            model_name='snippet',
            name='category',
            field=models.CharField(default=2020, max_length=200),
            preserve_default=False,
        ),
    ]
