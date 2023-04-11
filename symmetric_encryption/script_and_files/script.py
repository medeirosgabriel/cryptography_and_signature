import pandas as pd
import secrets
import csv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = bytearray.fromhex("5effc934f57c6832a19fcdfe9c358cbe")
nonce = bytearray.fromhex("8245248d6750f7efdda9e5c4b5288e53")
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))

decryptor = cipher.decryptor()
encryptor = cipher.encryptor()

data = []
with open("./118210822.csv", 'r', newline='') as file:
  csvreader = csv.reader(file, delimiter=',')
  for row in csvreader:
    # Decrypt
    n1, n2 = row
    n1 = int(decryptor.update(bytes.fromhex(n1)).decode())
    n2 = int(decryptor.update(bytes.fromhex(n2)).decode())
    # Sum
    sum = n1 + n2
    # Encrypt
    cipher_n1 = encryptor.update(str(n1).encode()).hex()
    cipher_n2 = encryptor.update(str(n2).encode()).hex()
    cipher_sum = encryptor.update(str(sum).encode()).hex()
    data.append([cipher_n1, cipher_n2, cipher_sum])

with open("./118210822_final.csv", 'w', newline='') as file:
  csvwriter = csv.writer(file, delimiter=',')
  csvwriter.writerows(data)