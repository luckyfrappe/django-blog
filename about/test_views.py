from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateRequestForm
from .models import About

class TestAboutPage(TestCase):
    def setUp(self):
        self.about = About(title = 'Greatest luckyfrappe',
                            content = 'This is about content',
                            profile_images = 'placeholder')
        self.about.save()

    def test_render_about_detail_page_with_collaborateform(self):
        response = self.client.get(reverse(
            'about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Greatest luckyfrappe", response.content)
        self.assertIn(b"This is about content", response.content)
        self.assertIsInstance(
            response.context['collaboration_form'], CollaborateRequestForm)
        
    def test_successful_collaboration_request_submission(self):
        post_data = {
            'name': 'Lolo',
            'email': 'lamour@gmail.com',
            'message': 'Lets collab!'
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Request submitted, we will get in touch shortly',
            response.content
        )