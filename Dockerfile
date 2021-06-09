FROM python:3.8.5
RUN mkdir /code
COPY requirements.txt /code
RUN pip3 install -r /code/requirements.txt
COPY . /code
WORKDIR /code
CMD gunicorn api_yamdb.wsgi:application --bind 84.252.143.224:8000