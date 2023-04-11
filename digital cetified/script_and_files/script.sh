openssl genrsa -out private.key 2048
openssl req -new -key private.key -out server.csr 
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ca.key -out ca.crt
openssl x509 -req -days 360 -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt