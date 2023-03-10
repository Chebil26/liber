# Generated by Django 4.1.3 on 2022-12-02 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=255)),
                ('publish_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('semester', models.CharField(choices=[('neuf_jamais_utilise', 'Neuf jamais utilisé'), ('neuf', 'Neuf'), ('bon', 'Bon')], default='neuf_jamais_utilise', max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
        ),
    ]
