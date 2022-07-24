FROM tiangolo/uwsgi-nginx-flask

ADD . /code
WORKDIR /code

ENTRYPOINT [ "python", "interview_app.py"]