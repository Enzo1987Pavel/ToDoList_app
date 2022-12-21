# Generated by Django 4.0.1 on 2022-12-21 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bot', '0002_alter_tguser_tg_chat_id_alter_tguser_tg_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tguser',
            name='tg_username',
        ),
        migrations.AlterField(
            model_name='tguser',
            name='tg_user_id',
            field=models.BigIntegerField(unique=True, verbose_name='id пользователя'),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь приложения'),
        ),
    ]