from django.conf import settings
from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_default_superuser(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    if not User.objects.filter(username='admin').exists():
        User.objects.create(
            username='admin',
            email='admin@noir.local',
            password=make_password('admin12345'),
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_categoria_remove_roupa_disponivel_and_more'),
    ]

    operations = [migrations.RunPython(create_default_superuser, migrations.RunPython.noop)]