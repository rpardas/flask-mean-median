FROM python:3.12-slim

WORKDIR /opt/app

RUN python3 -m venv /opt/app/flask-mean-median

COPY . .

RUN . /opt/app/flask-mean-median/bin/activate && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=api.py

CMD ["/opt/app/flask-mean-median/bin/python", "-m", "flask", "run", "--host=0.0.0.0"]