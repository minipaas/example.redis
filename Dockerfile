FROM ubuntu:13.10

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install less \
    uwsgi uwsgi-core uwsgi-plugin-python python-virtualenv python-dev

ADD service /etc/minipaas
ADD code /srv/autoincrement
RUN virtualenv /srv/ve && /srv/ve/bin/pip install -r /srv/autoincrement/requirements.txt

ENV minipaas_version 1

EXPOSE 80

ENTRYPOINT ["/usr/bin/uwsgi"]
CMD ["--plugins", "http,python", "--http", ":80", "--wsgi-file", "/srv/autoincrement/server.py", "--virtualenv", "/srv/ve" ]

