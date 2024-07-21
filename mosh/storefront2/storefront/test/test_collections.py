 
from rest_framework import status
from rest_framework.test import APIClient
# vaghti permission ro check mikone va masalan entezare khataye 401 ro dare va ma perrmission ro hazf mikonim baese erro mishe vase jelogiri darim:
import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
class Testcreatecollection:
    # movaghat bekhaim test nakone:
    # @pytest.mark.skip
    def test_userisananimous_401(self):
        # (aaa) arrange, act, assert
        # arrange:
        client=APIClient()
        response=client.post('/store/collections',{'title':'a'})

        # act:
        # assert response.status_code==status.HTTP_404_NOT_FOUND
        assert response.status_code==status.HTTP_401_UNAUTHORIZED
# vase continus testing: pip install pytest-watch
# ptw 
# user auth hast vali admin nist:
    def test_userisnotadmin_403(self):
    
        client=APIClient()
        client.force_authenticate(user={})
        response=client.post('/store/collections',{'title':'a'})
 
        assert response.status_code==status.HTTP_403_FORBIDDEN


# ettelaate eshtebah:
    def test_dataisinvalid_400(self):
 
        client=APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response=client.post('/store/collections',{'title':''})

        # act:
        # assert response.status_code==status.HTTP_404_NOT_FOUND
        assert response.status_code==status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_dataisvalid_201(self):
 
        client=APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response=client.post('/store/collections',{'title':'a'})

        # act:
        # assert response.status_code==status.HTTP_404_NOT_FOUND
        assert response.status_code==status.HTTP_201_CREATED
        assert response.data['id'] >0
# pip install modelbakery
@pytest.mark.django_db
class Testretrievecollection:
    def testifcollectionexestsreturn200(self,api_lient):
        baser.make(Product,)