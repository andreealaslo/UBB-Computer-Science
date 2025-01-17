# Generated by Django 4.1.7 on 2023-03-13 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('surface', models.CharField(max_length=100)),
                ('climate', models.CharField(max_length=100)),
                ('the_predominant_religion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('related_color', models.CharField(max_length=100)),
                ('someone_born_on_this_month', models.CharField(max_length=100)),
                ('a_grade', models.IntegerField()),
                ('an_animal_that_likes_this_season', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('a_person_to_complete_the_activity_with', models.CharField(max_length=100)),
                ('money_required', models.CharField(max_length=100)),
                ('time_required', models.CharField(max_length=100)),
                ('related_season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Activities.season')),
            ],
        ),
    ]
