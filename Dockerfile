FROM python:3

EXPOSE 8000

RUN pip install prometheus_client pythonping

ADD src /

CMD [ "python", "-u", "./pingmetrics.py" ]