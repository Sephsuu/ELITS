# Generated by Django 5.0.7 on 2024-07-22 00:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elitsBackend', '0003_officer_alter_merchandise_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('studentNumber', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('lastName', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(blank=True, max_length=50)),
                ('address', models.TextField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=255)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='elitsBackend.students')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
