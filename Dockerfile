FROM python:3.7-alpine

COPY app/twitterbot.py /app/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /app
CMD ["python3", "twitterbot.py"]
