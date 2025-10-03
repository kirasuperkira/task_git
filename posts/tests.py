from django.test import TestCase, Client
from .models import Post

class PostModelTest(TestCase):
   pass

class PostViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        Post.objects.create(title="Тест 1", content="Содержимое 1")
        Post.objects.create(title="Тест 2", content="Содержимое 2")

    def test_post_list_view_status(self):
        """Проверка, что страница /posts/ возвращает статус 200"""
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    # def test_post_list_view_status(self):
    #     response = self.client.get('/posts/')
    #     self.assertFalse(response.status_code == 200)

    def test_post_list_view_content(self):
        """Проверка, что на странице отображаются заголовки постов"""
        response = self.client.get('/posts/')
        self.assertContains(response, "Тест 1")
        self.assertContains(response, "Тест 2")

    def test_post_id_view_status(self):
        """Проверка, что пост существует"""
        response = self.client.get('/posts/')
        self.assertTrue(Post.objects.filter(pk=True).exists())

    def test_post_id_view_status(self):
        """Проверка, что страница /posts/ возвращает статус 200"""
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_id_view_content(self):
        """Проверка, что на странице отображаются заголовки постов"""
        response = self.client.get('/posts/')
        self.assertContains(response, "Тест 1")
        self.assertContains(response, "Тест 2")