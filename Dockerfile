FROM python:3.12-rc-slim-bullseye

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /sample .

CMD ["python3", "main.py"]