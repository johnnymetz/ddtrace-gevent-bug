# ddtrace + gevent bug

Project to demonstrate a bug with ddtrace and gevent.

Video Demo: https://www.loom.com/share/60d9c18fe7b04cca852a73bbac924b54

## Setup

Create venv and install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install - requirements.txt
```

Seed database:

```
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic --no-input
```

Configure environment variables:

```
cp env.sample .env
# fill out values in .env file
```

## Bug

Run the server with ddtrace, gunicorn and gevent. You don't need to have the datadog agent running (bug occurs with and without it). Then attempt to upload a file to S3 in the Django Admin.

```
ddtrace-run gunicorn mysite.wsgi --worker-class gevent --log-level debug
```

Upload a file. Notice the server crashes and the file is never uploaded to S3:

```
[DEBUG] POST /admin/bug/fileobject/add/
[CRITICAL] WORKER TIMEOUT (pid:32265)
[INFO] Worker exiting (pid: 32265)
[INFO] Booting worker with pid: 32418
```

## Other servers work fine

The following servers work fine:

```
./manage.py runserver
gunicorn mysite.wsgi
gunicorn mysite.wsgi --worker-class gevent
ddtrace-run ./manage.py runserver
ddtrace-run gunicorn mysite.wsgi
```
