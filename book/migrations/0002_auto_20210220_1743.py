# Generated by Django 3.1.6 on 2021-02-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='qty',
            field=models.CharField(max_length=64),
        ),
    ]