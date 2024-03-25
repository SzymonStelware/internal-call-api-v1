How to run internal-call-api-v1.py

#Make sure that port 1234 is open for the connection.

1. git clone https://github.com/SzymonStelware/internal-call-api-v1.git
2. docker build -t <my_application> -f docker/Dockerfile .
3. docker run -p 1234:1234 <my_application>
