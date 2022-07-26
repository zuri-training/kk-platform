# Generated by Django 4.0.5 on 2022-07-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('User_ID', models.CharField(max_length=100)),
                ('College_name', models.CharField(max_length=400)),
                ('Department', models.CharField(max_length=100)),
                ('Year_of_admission', models.CharField(max_length=20)),
                ('Year_of_graduation', models.CharField(max_length=20)),
                ('Account_verification', models.CharField(max_length=100)),
                ('Account_suspension_status', models.CharField(max_length=100)),
                ('User_tag', models.CharField(max_length=100)),
            ],
        ),
    ]
