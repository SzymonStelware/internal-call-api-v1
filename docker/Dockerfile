FROM python:3.8

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/SzymonStelware/internal-call-api-v1.git .

RUN pip install -r requirements.txt

CMD ["python", "internal-call-api-v1.py"]