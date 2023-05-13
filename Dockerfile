FROM python:3.11.0-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY . /app


RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/requirements.txt

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


# docker build -t django_image .
# docker run -p 8001:8000 --name django_container -d django_image
# docker exec -it django_container python3 manage.py makemigrations
# docker exec -it django_container python3 manage.py migrate

# docker rmi django_image
# docker image rm django_image
# docker ps
# docker container ls