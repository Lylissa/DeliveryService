# Generated by Django 3.0.5 on 2021-10-02 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClickToEat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='id',
            new_name='client_id',
        ),
    ]
