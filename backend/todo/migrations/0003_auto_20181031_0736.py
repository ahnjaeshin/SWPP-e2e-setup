# Generated by Django 2.1.1 on 2018-10-31 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20181031_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(),
        ),
    ]