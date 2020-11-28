FROM python:3

# Needed for printing of flask app to work
ENV FLASK_ENV="production" \
    PYTHONUNBUFFERED="true"

EXPOSE 8000
EXPOSE 8001

RUN pip install prometheus_client \
    pythonping \
    flask \
    flask_cors

ADD backend /backend



CMD [ "python", "-u", "/backend/api/pingerApi.py" ]
