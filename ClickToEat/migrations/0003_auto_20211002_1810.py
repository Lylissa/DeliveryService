# Generated by Django 3.0.5 on 2021-10-02 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClickToEat', '0002_auto_20211002_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
