# Generated by Django 4.0.4 on 2022-06-07 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('total_price', models.DecimalField(blank=True, decimal_places=4, max_digits=13, null=True)),
            ],
        ),
    ]
