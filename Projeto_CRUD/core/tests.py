from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Categoria, Modelo, Roupa
from .forms import CategoriaForm, ModeloForm


class CrudEdicaoTest(TestCase):
    def test_editar_roupa_com_sucesso(self):
        admin = get_user_model().objects.create_user(username='admin_test', password='senha-segura', is_staff=True, is_superuser=True)
        self.client.force_login(admin)
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

    def test_nao_permite_produto_duplicado(self):
        admin = get_user_model().objects.create_user(username='admin_duplicate', password='senha-segura', is_superuser=True)
        self.client.force_login(admin)
        categoria = Categoria.objects.create(categoria='Casual')
        Modelo.objects.create(modelo='Oversized', categoria=categoria)
        Roupa.objects.create(categoria=categoria, modelo=Modelo.objects.get(modelo='Oversized'), cor='Preto', tamanho='M', quantidade=2)

        response = self.client.post(
            reverse('criar_roupa'),
            {'categoria_text': 'Casual', 'modelo_text': 'Oversized', 'cor': 'preto', 'tamanho': 'm', 'quantidade': 3},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Este produto já existe no estoque')
        self.assertEqual(Roupa.objects.count(), 1)

    def test_alterar_estoque_soma_quantidade(self):
        admin = get_user_model().objects.create_user(username='admin_stock', password='senha-segura', is_superuser=True)
        self.client.force_login(admin)
        roupa = Roupa.objects.create(cor='Preto', tamanho='M', quantidade=2)

        response = self.client.post(
            reverse('alterar_estoque', args=[roupa.id]),
            {'operacao': 'adicionar', 'quantidade': 5},
        )

        self.assertRedirects(response, reverse('lista_roupas'))
        roupa.refresh_from_db()
        self.assertEqual(roupa.quantidade, 7)

    def test_alterar_estoque_subtrai_quantidade(self):
        admin = get_user_model().objects.create_user(username='admin_remove', password='senha-segura', is_superuser=True)
        self.client.force_login(admin)
        roupa = Roupa.objects.create(cor='Preto', tamanho='M', quantidade=5)

        response = self.client.post(
            reverse('alterar_estoque', args=[roupa.id]),
            {'operacao': 'subtrair', 'quantidade': 3},
        )

        self.assertRedirects(response, reverse('lista_roupas'))
        roupa.refresh_from_db()
        self.assertEqual(roupa.quantidade, 2)

    def test_alterar_estoque_nao_permite_quantidade_negativa(self):
        admin = get_user_model().objects.create_user(username='admin_negative', password='senha-segura', is_superuser=True)
        self.client.force_login(admin)
        roupa = Roupa.objects.create(cor='Preto', tamanho='M', quantidade=2)

        response = self.client.post(
            reverse('alterar_estoque', args=[roupa.id]),
            {'operacao': 'subtrair', 'quantidade': 3},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'não pode deixar o estoque negativo')
        roupa.refresh_from_db()
        self.assertEqual(roupa.quantidade, 2)

    def test_nao_permite_categoria_duplicada(self):
        Categoria.objects.create(categoria='Casual')

        form = CategoriaForm(data={'categoria': ' casual '})

        self.assertFalse(form.is_valid())
        self.assertIn('Esta categoria já está cadastrada.', form.errors['categoria'])

    def test_nao_permite_modelo_duplicado_na_mesma_categoria(self):
        categoria = Categoria.objects.create(categoria='Casual')
        Modelo.objects.create(modelo='Oversized', categoria=categoria)

        form = ModeloForm(data={'modelo': 'oversized', 'categoria_text': 'casual'})

        self.assertFalse(form.is_valid())
        self.assertIn('Este modelo já está cadastrado nesta categoria.', form.non_field_errors())


class PermissoesTest(TestCase):
    def test_usuario_comum_nao_pode_entrar_no_login_admin(self):
        get_user_model().objects.create_user(username='visitante', password='senha-segura')

        response = self.client.post(reverse('login'), {'username': 'visitante', 'password': 'senha-segura'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Apenas o superusuário pode entrar')

    def test_superusuario_entra_direto_na_tela_de_produtos(self):
        get_user_model().objects.create_superuser(username='admin_login', password='senha-segura')

        response = self.client.post(reverse('login'), {'username': 'admin_login', 'password': 'senha-segura'})

        self.assertRedirects(response, reverse('inicio'))

    def test_visitante_anonimo_precisa_fazer_login(self):
        response = self.client.get(reverse('inicio'))

        self.assertRedirects(response, f'{reverse("login")}?next={reverse("inicio")}')

    def test_admin_direto_exige_superusuario(self):
        user = get_user_model().objects.create_user(username='staff', password='senha-segura', is_staff=True)
        self.client.force_login(user)

        response = self.client.get('/admin/')

        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def test_usuario_comum_pode_visualizar_mas_nao_editar(self):
        user = get_user_model().objects.create_user(username='visitante', password='senha-segura')
        roupa = Roupa.objects.create(cor='Preto', tamanho='M', quantidade=2)
        self.client.force_login(user)

        self.assertEqual(self.client.get(reverse('lista_roupas')).status_code, 200)
        response = self.client.get(reverse('editar_roupa', args=[roupa.id]))

        self.assertEqual(response.status_code, 403)
