from django.test import TestCase

from main.models import Service

class ServiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Service.objects.create(code='TST',description='Test',typeserv='p',cost=5,comment='')

    def test_code(self):
        service = Service.objects.get(id=1)
        self.assertEquals(service.code,'TST')

    