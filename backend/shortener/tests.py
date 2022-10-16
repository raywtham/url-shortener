from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase
from shortener.models import ShortenedUrl


class ShortenedUrlTest(APITestCase):

    def setUp(self):
        # create shortened url object for testing
        ShortenedUrl.objects.create(long_url='www.apple.com', code="ABC123")

    def test_create_shortened_url_obj(self):
        url = api_reverse('api-shortener:shortened-create')
        data = {
            'long_url': 'http://www.yahoo.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['short_url'])

    def test_custom_url_validation(self):
        url = api_reverse('api-shortener:shortened-create')
        data = {
            'long_url': 'www.amazon.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['short_url'])

    def test_shortened_url_obj_redirect(self):
        obj = ShortenedUrl.objects.first()
        url = api_reverse('api-shortener:shortened-detail',
                          kwargs={'code': obj.code})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
