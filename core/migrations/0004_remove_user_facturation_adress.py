# Generated by Django 4.2.10 on 2024-02-27 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='facturation_adress',
        ),
    ]