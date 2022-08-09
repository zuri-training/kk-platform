# Generated by Django 4.0.5 on 2022-08-09 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_login_remove_user_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('College_name', models.CharField(max_length=400)),
                ('Department', models.CharField(max_length=100)),
                ('Year_of_admission', models.IntegerField(default='0')),
                ('Year_of_graduation', models.IntegerField(default='0')),
                ('Account_verification', models.CharField(max_length=100)),
                ('Account_suspension_status', models.CharField(max_length=100)),
                ('User_tag', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Password2', models.CharField(max_length=100)),
                ('last_login', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_ID_Front_View', models.ImageField(upload_to='idcards_frontview')),
                ('School_ID_Back_View', models.ImageField(upload_to='idcards_backview')),
                ('User_Main', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userapp.user_main')),
            ],
        ),
        migrations.CreateModel(
            name='Validation2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_Email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Login',
            new_name='Login_page',
        ),
        migrations.RemoveField(
            model_name='video',
            name='Video_Link',
        ),
        migrations.RemoveField(
            model_name='video_reaction',
            name='User',
        ),
        migrations.RemoveField(
            model_name='video_share',
            name='User',
        ),
        migrations.AddField(
            model_name='video',
            name='Video_File',
            field=models.FileField(default='1', upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='video_reaction',
            name='User_Main',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='userapp.user_main'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video_share',
            name='User_Main',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='userapp.user_main'),
            preserve_default=False,
        ),
    ]