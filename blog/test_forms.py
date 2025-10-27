from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'content': 'fdgd'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_isinvalid(self):
        comment_form = CommentForm({'content': ''})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid')