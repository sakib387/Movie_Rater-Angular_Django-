# Generated by Django 4.2.4 on 2023-09-17 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='descripiton',
            new_name='description',
        ),
    ]