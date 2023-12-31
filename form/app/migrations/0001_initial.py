# Generated by Django 4.2.7 on 2023-12-27 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Cname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Cfee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Sid', models.IntegerField(primary_key=True, serialize=False)),
                ('Sname', models.CharField(max_length=100)),
                ('Sclass', models.CharField(max_length=100)),
                ('Scourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
    ]
