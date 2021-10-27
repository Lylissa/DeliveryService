# Generated by Django 3.0.5 on 2021-10-02 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ClickToEat', '0008_rider_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='rider_id',
            new_name='store_id',
        ),
        migrations.AddField(
            model_name='store',
            name='rider',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ClickToEat.Rider'),
        ),
    ]
