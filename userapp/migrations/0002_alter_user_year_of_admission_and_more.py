# Generated by Django 4.0.5 on 2022-07-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Year_of_admission',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Year_of_graduation',
            field=models.IntegerField(default='0'),
        ),
    ]
