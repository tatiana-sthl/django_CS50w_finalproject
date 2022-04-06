# Generated by Django 4.0.3 on 2022-04-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_follows_alter_user_profile_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(upload_to='', verbose_name='profile picture'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CREATOR', 'Créateur'), ('SUBSCRIBER', 'Abonné')], max_length=30, verbose_name='role'),
        ),
    ]