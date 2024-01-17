FROM python:3.12.1-slim
COPY app .
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN rm -rf .cache/pip
CMD exec gunicorn --bind :8080 --workers 2 main:app