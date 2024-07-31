from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.view_class, HomePageView)
        
    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('politics',)) 
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200)

    def test_detail_view_status_code(self):
        url = reverse('news-detail', args=[2024,3,19,'test'])
        print("\n-------============------")
        print(url)
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200) # why error?




