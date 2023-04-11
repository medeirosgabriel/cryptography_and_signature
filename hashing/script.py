import hashlib
from cryptography.hazmat.primitives import hashes

with open('file.txt', 'w') as file:
  file.write("Atividade 2 - Hashing Com Python - Gabriel Medeiros")

final_digestor = hashlib.sha256()

with open('file.txt', 'rb') as file:
  chunk = file.read(5)

  while chunk:
    final_digestor.update(chunk)
    chunk = file.read(5)

hash = final_digestor.hexdigest()

print(hash) # d28b077f1ddea9dd3544bf475fdef3befe8b9dc246465745dca53e04fc75c1f5