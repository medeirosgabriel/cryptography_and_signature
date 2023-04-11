openssl genrsa -out private_key.pem 2048
openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem

echo "118210822" | openssl pkeyutl -encrypt -inkey private_key.pem -out file.txt.enc
openssl pkeyutl -decrypt -inkey ./private_key.pem -in file.txt.enc -out file_dec.txt
