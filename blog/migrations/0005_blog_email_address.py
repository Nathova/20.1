# Generated by Django 4.2.4 on 2023-08-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='email_address',
            field=models.CharField(default='не указано', max_length=100, verbose_name='электронная почта'),
        ),
    ]
