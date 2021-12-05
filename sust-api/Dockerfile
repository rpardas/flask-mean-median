FROM python:3.7

WORKDIR /opt/app

# RUN python3 -m venv /opt/app/sustenv

COPY . .


RUN . /opt/app/sustenv/bin/activate && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]