from django.test import TestCase

from .models import Post


# Create your tests here.


class ModelTesting(TestCase):

    def setUp(self) -> None:
        self.post = Post.objects.create(
            title = 'Python',
            author = 'Jetkerpy',
            slug = 'python'
        )

    
    def test_post_model(self):
        d = self.post
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'Python')





    

