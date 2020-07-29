FROM python:3

ADD alert.py /

RUN pip install flask

RUN pip install requests

EXPOSE 5000

CMD [ "python", "./alert.py" ]