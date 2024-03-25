FROM python:latest

WORKDIR /app
COPY . /api /app/

RUN pip3 install flask requests

EXPOSE 1234

CMD ["python", "internal-call-api-v1.py"]