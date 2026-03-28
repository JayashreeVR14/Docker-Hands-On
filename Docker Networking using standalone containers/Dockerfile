FROM python:3.9

WORKDIR /app

COPY app/ /app
COPY requirements/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
