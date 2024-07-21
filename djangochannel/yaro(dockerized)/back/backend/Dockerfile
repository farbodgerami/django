FROM python:3.9.7-slim 
ENV PYTHONUNBUFFERED 1

RUN pip install pip --upgrade 

RUN mkdir app
WORKDIR /app
COPY . /app
RUN pip install django
RUN pip install channels
RUN pip install daphne
RUN pip install channels-redis==4.0.0
# RUN pip install -r r.txt 
 
EXPOSE 8000 

# CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
CMD ["daphne", "core.routing:application","-b","0.0.0.0","-p","8000"]


#  gunicorn backend.wsgi:application --bind 0.0.0.0:7000

# channels==4.0.0
# channels-redis==4.0.0

# redis==4.4.0

