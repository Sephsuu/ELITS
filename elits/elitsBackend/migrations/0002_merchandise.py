# Generated by Django 5.0.7 on 2024-07-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elitsBackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('originalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discountPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(choices=[('Lanyard', 'Lanyard'), ('T-shirt', 'T-shirt'), ('Others', 'Others')], max_length=255)),
                ('size', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=255)),
                ('merchImage', models.ImageField(upload_to='merchandiseImage')),
            ],
        ),
    ]
