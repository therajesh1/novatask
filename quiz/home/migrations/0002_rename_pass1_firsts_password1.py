# Generated by Django 5.0.6 on 2024-08-05 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firsts',
            old_name='pass1',
            new_name='password1',
        ),
    ]
