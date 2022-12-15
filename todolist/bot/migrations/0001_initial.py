# Generated by Django 4.0.1 on 2022-12-15 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_chat_id', models.BigIntegerField(verbose_name='tg_chat_id')),
                ('tg_user_id', models.BigIntegerField(unique=True, verbose_name='tg_user_id')),
                ('username', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='tg_username')),
                ('verification_code', models.CharField(max_length=8, unique=True, verbose_name='Код подтверждения')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Telegram пользователь',
                'verbose_name_plural': 'Telegram пользователи',
            },
        ),
    ]
