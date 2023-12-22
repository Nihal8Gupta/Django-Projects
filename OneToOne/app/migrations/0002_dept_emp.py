# Generated by Django 4.2.7 on 2023-12-08 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DEPT',
            fields=[
                ('DEPT_Name', models.CharField(max_length=100)),
                ('DEPT_No', models.IntegerField(primary_key=True, serialize=False)),
                ('LOC', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('EMP_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('EMP_Name', models.CharField(max_length=100)),
                ('LOC', models.CharField(max_length=100)),
                ('DEPT_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]