# Generated by Django 5.0.2 on 2024-03-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0007_extrainfo_owner_film_owner_ocena_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='imdb_pkts',
            new_name='imdb_points',
        ),
        migrations.RenameField(
            model_name='filmmodellab4',
            old_name='imdb_pkts',
            new_name='imdb_points',
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(4, 'Dramat'), (1, 'Horror'), (0, 'Inne'), (3, 'Sci-fi'), (2, 'Komedia')], null=True),
        ),
    ]
