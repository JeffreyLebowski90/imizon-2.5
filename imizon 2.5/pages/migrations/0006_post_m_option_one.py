# Generated by Django 2.1.3 on 2019-01-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20190108_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='m_option_one',
            field=models.CharField(default='empty', max_length=100),
        ),
    ]
