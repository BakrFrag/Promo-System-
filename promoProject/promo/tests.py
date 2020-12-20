from rest_framework.test import force_authenticate,APIClient;
import unittest;
from django.urls import reverse;
class TestPromoViewset(unittest.TestCase):
    def setUp(self):
    
        self.client=APIClient();
        self.client.login(username='bk',password='147');
    def test_list(self):
        # Test retrieve list of objects 
        response=self.client.get(reverse('promo_list'));
        self.assertEqual(response.status_code,200);
        # Test retrieve specfic object
        response=self.client.get(reverse('promo_list'),kwargs={'pk':7,'q':'remaining'});
        print(response.status_code)
        self.assertEqual(response.status_code,200);
    def test_delete(self):
        response=self.client.delete(reverse('delete_promo',kwargs={"pk":100}));
        print(response.status_code)
        self.assertEqual(response.status_code,404);
    def test_partial_update(self):
       
        response=self.client.patch(reverse('promo_partial_update',kwargs={
            "pk":5
        }),{"amount":1000});
        self.assertEqual(response.status_code,403);
class testPromoNormalUser(unittest.TestCase):
    def setUp(self):
    
        self.client=APIClient();
        self.client.login(username='normal1',password='normal147258369');
    def test_list(self):
        # Test retrieve list of objects 
        response=self.client.get(reverse('promo_list'));
        self.assertEqual(response.status_code,200);
        # Test retrieve specfic object
        response=self.client.get(reverse('promo_list'),kwargs={'pk':7,'q':'remaining'});
        print(response.status_code)
        self.assertEqual(response.status_code,200);
    def test_delete(self):
        response=self.client.delete(reverse('delete_promo',kwargs={"pk":100}));
        print(response.status_code)
        self.assertEqual(response.status_code,403);
    def test_partial_update(self):
       
        response=self.client.patch(reverse('promo_partial_update',kwargs={
            "pk":100
        }),{"amount":1000});
        self.assertEqual(response.status_code,404);


