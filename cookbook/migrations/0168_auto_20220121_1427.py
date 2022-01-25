# Generated by Django 3.2.11 on 2022-01-21 20:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import cookbook.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook', '0167_userpreference_left_handed'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[('RECIPE', 'Recipe'), ('FOOD', 'Food'), ('KEYWORD', 'Keyword')], default=('RECIPE', 'Recipe'), max_length=128)),
                ('search', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shared', models.ManyToManyField(blank=True, related_name='f_shared_with', to=settings.AUTH_USER_MODEL)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.space')),
            ],
            bases=(models.Model, cookbook.models.PermissionModelMixin),
        ),
        migrations.AddConstraint(
            model_name='customfilter',
            constraint=models.UniqueConstraint(fields=('space', 'name'), name='cf_unique_name_per_space'),
        ),
        migrations.AddField(
            model_name='recipebook',
            name='filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cookbook.customfilter'),
        ),
    ]
