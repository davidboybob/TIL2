# Generated by Django 2.2.6 on 2019-10-19 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='creeated_at',
            new_name='created_at',
        ),
    ]
