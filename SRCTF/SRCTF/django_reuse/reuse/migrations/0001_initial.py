# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 14:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('typename', models.CharField(max_length=100)),
                ('description', models.TextField(default='TBD')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('is_solved', models.BooleanField()),
                ('flag', models.CharField(max_length=200)),
                ('c_dir', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ctf_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=50)),
                ('src_path', models.CharField(default='not_a_dir', max_length=200)),
                ('gen_path', models.CharField(default='not_a_gen', max_length=200)),
                ('desc', models.TextField(default='TBD')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reuse.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Ctf_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reuse.Ctf_info')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_granted', models.BooleanField()),
                ('u_dir', models.CharField(max_length=200)),
                ('status', models.IntegerField(default='1')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ctf_tag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reuse.Tag'),
        ),
        migrations.AddField(
            model_name='ctf_info',
            name='tags',
            field=models.ManyToManyField(through='reuse.Ctf_Tag', to='reuse.Tag'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='ctf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reuse.Ctf_info'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='ctype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reuse.Type'),
        ),
        migrations.AddField(
            model_name='category',
            name='tags',
            field=models.ManyToManyField(through='reuse.Cat_Tag', to='reuse.Tag'),
        ),
        migrations.AddField(
            model_name='cat_tag',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reuse.Category'),
        ),
        migrations.AddField(
            model_name='cat_tag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reuse.Tag'),
        ),
    ]