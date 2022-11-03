# Generated by Django 4.1.2 on 2022-10-20 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_day', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TypeMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_descript', models.TextField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plans.day')),
                ('type_meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plans.typemeal')),
            ],
        ),
    ]
