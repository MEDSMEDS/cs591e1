# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualProblemResults',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('ProblemNo', models.IntegerField()),
                ('Operand1', models.IntegerField()),
                ('Operand2', models.IntegerField()),
                ('Operation', models.CharField(max_length=2)),
                ('AnsweredCorrectly', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='tests',
            fields=[
                ('Test_ID', models.AutoField(primary_key=True, serialize=False)),
                ('problem', models.CharField(max_length=50)),
                ('Score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('User_ID', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=50)),
                ('PassWord', models.CharField(max_length=50)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='tests',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.users'),
        ),
        migrations.AddField(
            model_name='individualproblemresults',
            name='Test_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.tests'),
        ),
    ]
