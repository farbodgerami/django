# from django.test import TestCase
# from ..models import Post,Category
# from accounts.models import User
# from datetime import datetime

# class TestPostModel(TestCase):
#     def setUp(self):
#         self.user=User.objects.create_user(email='test@test.com',password='aaaaaaaadfqwerigo3234523')

#     def testcreatepostwithvaliddata(self):

#         post=Post.objects.create(title='test',author=self.user,content="aaaaaaaaaaa",status=True,category=None,published_date=datetime.now())
#         self.assertEquals(post.title,'test')
#         self.assertTrue(Post.objects.filter(pk=post.id).exists())
