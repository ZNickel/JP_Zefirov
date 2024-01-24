# Generated by Django 5.0.1 on 2024-01-23 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('salary_from', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_to', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_currency', models.CharField(blank=True, max_length=3, null=True)),
                ('avg_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employer', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='VacancySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.skill')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.vacancy')),
            ],
        ),
    ]
