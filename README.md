How to run internal-call-api-v1.py

#Make sure that port 1234 is open for the connection.

#Docker Build
#Preparation --->
#1. docker build -t internal-call-api-v1:my_api -f docker/Dockerfile .
#2. docker tag internal-call-api-v1:my_api salmedd55/internal-call-api-v1:my_api
#3. docker push salmedd55/internal-call-api-v1:my_api

1. git clone https://github.com/SzymonStelware/internal-call-api-v1.git
2. docker build -t inernal-call-api-v1:my_api -f docker/Dockerfile .
3. docker run -p 1234:1234 inernal-call-api-v1:my_api
4. push docker img

#Kubernetes

1. install miniKube
2. run deployment.yaml -> kubectl apply -f deployment.yaml


#SQLite installation
For MacOs
--- download sqlite-autoconf-*.tar.gz from https://www.sqlite.org/download.html ---
$tar xvfz sqlite-autoconf-3071502.tar.gz
$cd sqlite-autoconf-3071502
$./configure --prefix=/usr/local
$make
$make install
$sqlite3 MyDB.db