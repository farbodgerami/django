from django.test import TestCase
from datetime import date,timedelta
import datetime
from .models import User
class paytest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='test')
        self.user.save()

    def testhaspaid(self):
        self.assertFalse(self.user.haspaid(),'bayad empty bashad')
    
    def testdiffrentdatevalues(self):
        currentdate=date(2020,1,4)
        _30days=timedelta(days=30)
        self.user.paidnuntil=currentdate +_30days
        self.assertTrue(self.user.haspaid(currentdate=currentdate))

    def testdifferentinputtypes(self):
        currentdate=datetime.date(2020,4,1)         
        _30days=timedelta(days=30)
        tsinfuture=currentdate +_30days
        # self.user.setpaiduntil(int(tsinfuture))
        self.user.setpaiduntil('1212344545')
