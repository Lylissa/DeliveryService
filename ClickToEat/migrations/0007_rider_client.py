# Generated by Django 3.0.5 on 2021-10-02 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ClickToEat', '0006_auto_20211002_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='rider',
            name='client',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ClickToEat.Client'),
        ),
    ]
