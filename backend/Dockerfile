FROM python:3.8.8

RUN apt-get update

WORKDIR /app
COPY . /app
RUN export GOOGLE_APPLICATION_CREDENTIALS=google-credential.json
RUN pip install --upgrade pip
RUN pip install -r requirement.txt

EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]