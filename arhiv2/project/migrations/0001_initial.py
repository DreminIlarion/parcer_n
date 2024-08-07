# Generated by Django 5.0.3 on 2024-04-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Komerc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('information', models.TextField(blank=True, db_index=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('area', models.FloatField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('datas', models.DateTimeField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'komerc',
                'managed': False,
            },
        ),
    ]
