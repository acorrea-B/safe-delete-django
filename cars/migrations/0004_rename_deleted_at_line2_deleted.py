# Generated by Django 3.2.9 on 2021-11-30 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car2_line'),
    ]

    operations = [
        migrations.RenameField(
            model_name='line2',
            old_name='deleted_at',
            new_name='deleted',
        ),
    ]
