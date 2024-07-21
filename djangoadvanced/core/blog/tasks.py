from celery import shared_task
from time import sleep

 
@shared_task
def sendemail():
 
    sleep(3)
    for i in range(100):
        print(i)
    print('a')
    print("Sending Mail")

# ino mizarim too dockercompose
# docker-compose exec backend1 sh -c "celery -A core worker --loglevel=info"

# docker-compose exec backend1 sh -c "celery -A core beat --loglevel=info"
# install celery beat
# makemigrations
# celery -A core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
