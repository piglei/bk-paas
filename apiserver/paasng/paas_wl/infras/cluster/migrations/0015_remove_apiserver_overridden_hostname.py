# Generated by Django 4.2.16 on 2024-12-28 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0014_migration_overridden_hostname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiserver',
            name='overridden_hostname',
        ),
    ]