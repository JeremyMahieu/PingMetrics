FROM python:3

EXPOSE 8000

RUN pip install prometheus_client pythonping flask flask_cors

ADD backend /backend

# Needed for printing of flask app to work
ARG FLASK_ENV="production"
ENV FLASK_ENV="${FLASK_ENV}" \
    PYTHONUNBUFFERED="true"

CMD [ "python", "-u", "/backend/api/pingerApi.py" ]