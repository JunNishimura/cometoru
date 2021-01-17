# Generated by Django 3.0.6 on 2021-01-12 07:14

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='prof_img',
            field=models.ImageField(blank=True, default='user/default.png', null=True, upload_to=user.models.get_image_path, verbose_name='プロフィール画像'),
        ),
    ]
