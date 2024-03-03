# Generated by Django 4.2.4 on 2024-02-27 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('radius', models.IntegerField()),
                ('habitable', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('radius', models.IntegerField()),
                ('temperature', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('radius', models.IntegerField()),
                ('habitable', models.BooleanField()),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.planet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('planet', models.ManyToManyField(to='core.planet')),
            ],
        ),
        migrations.AddField(
            model_name='planet',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.star'),
        ),
    ]
