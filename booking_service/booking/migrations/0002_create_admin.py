# Generated by Django 3.1.4 on 2020-12-14 10:35

from django.contrib.auth import get_user_model
from django.db import migrations


def generate_superuser(apps, schema_editor):
    """Сгенерировать суперпользователя для первого входа в приложение"""
    user_model = get_user_model()

    if not user_model.objects.count():
        user_model.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin'
        )
        print('\nUser "admin" has been created.')
    else:
        print('\nUsers exist. "Create admin" migration skipped.')


class Migration(migrations.Migration):
    """Миграция используется только для ПЕРВОГО ЗАПУСКА приложения"""

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_superuser, reverse_code=migrations.RunPython.noop),
    ]