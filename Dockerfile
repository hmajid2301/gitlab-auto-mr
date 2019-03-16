FROM python:alpine3.6
LABEL MAINTAINER="Haseeb Majid <me@haseebmajid.com>"

COPY dist/ ./
RUN ls -l
RUN pip install dist/*

