# Generated by Django 3.1.1 on 2020-11-12 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0007_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuageCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type_of_project', models.CharField(max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='projects',
            name='project',
        ),
        migrations.DeleteModel(
            name='Toy',
        ),
        migrations.AddField(
            model_name='snippet',
            name='type',
            field=models.CharField(default='method', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='projects',
        ),
    ]
