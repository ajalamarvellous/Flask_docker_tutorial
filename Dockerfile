FROM python:3.8.2-slim

RUN pip install --upgrade pip

WORKDIR /app
COPY ["deployment.py", "requirements.txt", "assets", "/"]

RUN pip install -r /requirements.txt

EXPOSE 1200

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:1200", "deployment:app"]
