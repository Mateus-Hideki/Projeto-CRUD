from django.test import TestCase
from django.urls import reverse

from .models import Categoria, Modelo, Roupa


class CrudEdicaoTest(TestCase):
    def test_editar_roupa_com_sucesso(self):
        categoria = Categoria.objects.create(categoria='Casual')
        modelo = Modelo.objects.create(modelo='Oversized', categoria=categoria)
        roupa = Roupa.objects.create(
            categoria=categoria,
            modelo=modelo,
            cor='Preto',
            tamanho='M',
            quantidade=5,
        )

        response = self.client.get(reverse('editar_roupa', args=[roupa.id]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse('editar_roupa', args=[roupa.id]),
            {
                'categoria_text': 'Premium',
                'modelo_text': 'Relaxed',
                'cor': 'Cinza',
                'tamanho': 'G',
                'quantidade': 8,
            },
        )

        self.assertRedirects(response, reverse('lista_roupas'))

        roupa.refresh_from_db()
        self.assertEqual(roupa.cor, 'Cinza')
        self.assertEqual(roupa.tamanho, 'G')
        self.assertEqual(roupa.quantidade, 8)
        self.assertEqual(roupa.categoria.categoria, 'Premium')
        self.assertEqual(roupa.modelo.modelo, 'Relaxed')
