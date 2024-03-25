FROM python:3.8
EXPOSE 1234

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/SzymonStelware/internal-call-api-v1.git .

RUN pip3 install flask requests

CMD ["python", "api/internal-call-api-v1.py"]