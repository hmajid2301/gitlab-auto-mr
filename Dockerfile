FROM python:alpine3.6
LABEL MAINTAINER="Haseeb Majid <me@haseebmajid.com>"

COPY dist ./dist/
RUN pip install dist/*

