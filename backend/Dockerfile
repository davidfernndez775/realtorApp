FROM python:3.13.1-alpine3.20
LABEL maintainer="davidfernndez775"

# to print Python messages in the console
ENV PYTHONUNBUFFERED 1

# copy the requirements files in the container
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# copy the app folder and set the port in the container
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# set DEV in false, this can be change by the docker-compose file
ARG DEV=false

# install the dependencies for database management and the requirements files 
# set a user with less priviligies
# create the volumes for media and static files
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev zlib zlib-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser -D -H -s /bin/false django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    mkdir -p /home/django-user && \
    chown -R django-user:django-user /vol && \
    chown -R django-user:django-user /home/django-user && \
    chmod -R 755 /vol

ENV PATH="/py/bin:$PATH"

USER django-user