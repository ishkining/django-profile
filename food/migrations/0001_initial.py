# Generated by Django 4.1.7 on 2023-02-24 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.IntegerField(max_length=4)),
                ('protein', models.IntegerField(max_length=4)),
                ('carbohydrates', models.IntegerField(max_length=4)),
                ('fat', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Consumed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grams', models.IntegerField(max_length=3)),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.product')),
            ],
        ),
    ]
