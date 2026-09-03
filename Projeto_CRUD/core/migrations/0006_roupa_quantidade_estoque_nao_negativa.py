from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0005_roupa_unique_produto_estoque'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='roupa',
            constraint=models.CheckConstraint(
                condition=models.Q(('quantidade__gte', 0)),
                name='quantidade_estoque_nao_negativa',
            ),
        ),
    ]