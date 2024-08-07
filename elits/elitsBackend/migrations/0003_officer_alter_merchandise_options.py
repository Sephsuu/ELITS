# Generated by Django 5.0.7 on 2024-07-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elitsBackend', '0002_merchandise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('officerImage', models.ImageField(blank=True, upload_to='officerImages')),
            ],
        ),
        migrations.AlterModelOptions(
            name='merchandise',
            options={'verbose_name_plural': 'Merchandise'},
        ),
    ]
