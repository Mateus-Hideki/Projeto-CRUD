from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0004_alter_roupa_categoria_alter_roupa_modelo'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='roupa',
            constraint=models.UniqueConstraint(
                fields=('modelo', 'cor', 'tamanho'),
                name='unique_produto_estoque',
            ),
        ),
    ]