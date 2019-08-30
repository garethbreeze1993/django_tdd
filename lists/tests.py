from django.test import TestCase

class HomePageTest(TestCase):
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html') # this is django specific test that says that this specific template was used when the appliucation hit that url above
        
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        
