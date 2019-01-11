# Generated by Django 2.1.5 on 2019-01-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20190110_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping', models.CharField(default='empty', max_length=100)),
                ('shipping_arrangement', models.CharField(default='empty', max_length=100)),
                ('payment', models.CharField(default='empty', max_length=100)),
            ],
        ),
    ]
