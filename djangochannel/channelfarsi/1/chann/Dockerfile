FROM python:slim-bullseye
RUN pip install pip --upgrade 
WORKDIR /app
COPY ./r.txt /app
 
 
 
RUN pip install -r r.txt 
# RUN pip install django==4.1.0
# RUN pip install -U channels["daphne"]
# RUN pip install channels_redis

COPY . /app
 
EXPOSE 8000
# CMD ["gunicorn","-w","1", "notification.wsgi:application","--bind","0.0.0.0:8000"]
# CMD ["daphne", "notification.asgi:application","-b","0.0.0.0","-p","8000"]
CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
# CMD ["python", "manage.py","runserver"]


#  gunicorn notification.wsgi:application --bind 0.0.0.0:7000

# daphne notification.asgi:application --bind 0.0.0.0:8000

 
# function sync va time.sleep(second)
# gunicorn -w 1: in mesle yek karmand avval raft sare yek tab. 1 sania vaisad va bade sh raft sare badi 
# daphne: hame ba ham sare 1 sanie vaisadan
# runserver: hame ba ham sare 1 sanie vaisadan

# function async va time.sleep(second)
# gunicorn -w 1: in mesle yek karmand avval raft sare yek tab. 1 sania vaisad va bade sh raft sare badi 
# daphne: in kheili ajib az tabe 1 ta 6 mashghool boodan va vaghti hame ba ham 6 sanie gozasht ba ham vaisadan
# runserver: hame ba ham sare 1 sanie vaisadan

# function async va asyncio.sleep()
# gunicorn -w 1: in mesle yek karmand avval raft sare yek tab. 1 sania vaisad va bade sh raft sare badi 
# daphne: hame ba ham sare 1 sanie vaisadan
