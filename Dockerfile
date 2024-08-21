FROM python:3.11.9 AS builder

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]