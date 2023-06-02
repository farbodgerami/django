 
FROM python:3.8-slim-buster
RUN pip install pip --upgrade 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY ./core /app/

# EXPOSE 8000 
# CMD ["python", "manage.py","runserver","0.0.0.0:8000"]

# create image:
# docker build -t dockerdjango . 
# start a container:
# docker run -d -p 8000:8000 --name mydj dockerdjango 
# docker rmi bb4
# vase app jadid docker-compose exec backend sh -c "python manage.py startapp blog"