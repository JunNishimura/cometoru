# Generated by Django 3.0.6 on 2020-12-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_delete_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='prof_img',
            field=models.ImageField(blank=True, default='user/default.png', null=True, upload_to='user/', verbose_name='プロフィール画像'),
        ),
    ]