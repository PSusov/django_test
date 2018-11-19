from django.test import TestCase
from main.models import Service
from django.urls import reverse

class ServiceListViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        for i in range(15):
            Service.objects.create(code='TST{0}'.format(i),description='Test {0}'.format(i),typeserv='p',cost=5,comment='')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/main/services/')
        self.assertEqual(resp.status_code,302)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('services'))
        self.assertEqual(resp.status_code,302)

    def test_view_uses_correct_template(self):
        resp = self.client.get('/main/services')
        self.assertEqual(resp.status_code,302)
        print(resp)
        self.assertTemplateUsed(resp, 'main/service_list.html')