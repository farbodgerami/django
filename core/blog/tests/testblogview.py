# from django.test import TestCase,Client
# from django.urls import reverse
# class TestBlogView(TestCase):
#     def setUp(self):
#         self.client=Client()

#     def test_blogindexurlresponsesuccess(self):
#         url =reverse('blog:api-v1:post-list')
#         response =self.client.get(path='http://localhost:8000/blog/api/v1/post/')
#         self.assertEqual(response.status_code,200)
#         print('rrrrrrrrrrrrrrrrrrrrrrrrr',response.content)

#         self.assertTrue(str(response.content).find("james"))
