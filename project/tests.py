from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import PerevalSerializer
from .models import *
from django.urls import reverse


class PerevallTest(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(

            status='',

            beauty_title='Test1',
            title='Test1',
            other_titles='Test1',
            connect='',

            tourist_id=Users.objects.create(
                email='test1@mail.ru',
                last_name='Test1',
                first_name='Test1',
                patronymic='Test1',
                phone='79998837756'
            ),

            coord_id=Coords.objects.create(
                latitude=56.000000,
                longitude=65.000000,
                height=2655
            ),
            level=Level.objects.create(
                winter_lev='4A',
                summer_lev='',
                autumn_lev='',
                spring_lev=''
            ),
        )
        self.image_1 = Images.objects.create(
            image="",
            title="Test1",
            pereval_id=self.pereval_1
        )
    def test_get_list(self):
        url = reverse('perevals-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1], many=True).data
        print('************')
        print(serializer_data)
        print('************')
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

