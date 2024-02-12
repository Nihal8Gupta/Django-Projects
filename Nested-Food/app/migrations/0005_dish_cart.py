# Generated by Django 5.0.1 on 2024-02-09 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_team_options_alter_category_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.PositiveIntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dish')),
            ],
        ),
    ]
