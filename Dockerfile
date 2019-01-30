FROM python:3.6

RUN pip install pipenv

ADD . /app
WORKDIR /app

RUN pipenv install --system --deploy

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "webserver"]
