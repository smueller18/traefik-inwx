FROM traefik:1.6-alpine

LABEL maintainer="Stephan Müller"

RUN apk add --no-cache python3

RUN mkdir -p /opt && \
    apk add --no-cache --virtual .build-deps curl && \
    curl -sSL https://raw.githubusercontent.com/inwx/python2.7-client/master/inwx.py -o /opt/inwx.py && \
    apk del .build-deps

COPY acme.py /opt/acme.py
ENV EXEC_PATH /opt/acme.py