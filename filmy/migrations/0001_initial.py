# Generated by Django 5.0.2 on 2024-02-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=64, unique=True)),
                ('rok', models.PositiveSmallIntegerField()),
                ('opis', models.TextField(default='')),
                ('premiera', models.DateField(blank=True, null=True)),
                ('imdb_pkts', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
    ]
