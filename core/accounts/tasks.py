from celery import shared_task
from django.http import HttpResponse
import time
 
# Create your views here.
@shared_task
def sendEmail():
    for i in range(2):

      time.sleep(1)
      print(i)
    # return "aaaaaaaaaaaaaaaaaadone"
 


# ino mizarim too dockercompose
# docker-compose exec backend1 sh -c "celery -A core worker --loglevel=info"

# docker-compose exec backend1 sh -c "celery -A core beat --loglevel=info"
# install celery beat
# makemigrations
# celery -A core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

# docker-compose exec backend1 sh -c "celery -A core beat --loglevel=info"

# celery-beat va django-celery-beat dar har do bayad nasb beshan vase jadvale task ha. dar installed apps ham ezafe beshe