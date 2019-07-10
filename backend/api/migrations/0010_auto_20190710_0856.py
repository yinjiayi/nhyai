# Generated by Django 2.1.2 on 2019-07-10 00:56

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190704_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileImageTerrorismUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datafile1', models.ImageField(blank=True, max_length=255, null=True, upload_to=api.models.path_and_rename)),
                ('result1', models.TextField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='FileVisionPornUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datafile2', models.ImageField(blank=True, max_length=255, null=True, upload_to=api.models.path_and_rename)),
                ('result2', models.TextField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='VideoFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datafile', models.FileField(blank=True, max_length=255, null=True, upload_to=api.models.path_and_rename)),
                ('width', models.PositiveIntegerField(editable=False, null=True)),
                ('height', models.PositiveIntegerField(editable=False, null=True)),
                ('duration', models.FloatField(editable=False, null=True)),
                ('count', models.PositiveIntegerField(editable=False, null=True)),
                ('result', models.TextField(default='', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='result',
            field=models.TextField(default='', max_length=256),
        ),
    ]
