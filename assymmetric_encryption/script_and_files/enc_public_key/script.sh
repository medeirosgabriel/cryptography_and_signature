openssl genrsa -out private_key.pem 2048
openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem

echo "118210822" | openssl rsautl -encrypt -pubin -inkey ./public_key.pem > file.txt.enc
openssl rsautl -decrypt -in ./file.txt.enc -out ./file_dec.txt -inkey ./private_key.pem