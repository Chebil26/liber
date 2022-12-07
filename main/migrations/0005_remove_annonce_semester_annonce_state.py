# Generated by Django 4.1.3 on 2022-12-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_annonce_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annonce',
            name='semester',
        ),
        migrations.AddField(
            model_name='annonce',
            name='state',
            field=models.CharField(choices=[('Neuf jamais utilisé', 'Neuf jamais utilisé'), ('Neuf', 'Neuf'), ('Bon', 'Bon')], default='neuf_jamais_utilise', max_length=20),
        ),
    ]
