# Generated by Django 3.1.6 on 2021-02-20 22:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
                ('unit', models.CharField(max_length=64)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('source', models.CharField(max_length=256)),
                ('steps', models.TextField()),
                ('tries', models.IntegerField(default=0)),
                ('icon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.icon')),
                ('ingredients', models.ManyToManyField(through='book.Measurement', to='book.Ingredient')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('date_modified', models.DateField(auto_now=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='measurement',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.recipe'),
        ),
    ]