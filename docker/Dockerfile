FROM python:3.8

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/SzymonStelware/internal-call-api-v1.git .

RUN pip3 install -r flask requests

CMD ["python", "internal-call-api-v1.py"]