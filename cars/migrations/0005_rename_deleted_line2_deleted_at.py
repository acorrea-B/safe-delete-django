# Generated by Django 3.2.9 on 2021-11-30 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_rename_deleted_at_line2_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='line2',
            old_name='deleted',
            new_name='deleted_at',
        ),
    ]