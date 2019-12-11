FROM python:3.8.0-alpine

COPY main.py /
COPY sorted_join /sorted_join

ENTRYPOINT ["/main.py"]