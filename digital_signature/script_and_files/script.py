from cryptography.hazmat.primitives import serialization

with open("./private_key.pem", "rb") as key_file:

    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

mensagem = b"118210822olatudobem"

signature = private_key.sign(
    mensagem,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256() # O HashAlgorithm também pode ser Prehashed
                    # caso o dado já tenha passado por hashing.
)

print(signature.hex())

public_key = private_key.public_key()

from cryptography.exceptions import InvalidSignature

try:
  mensagem_verificada = public_key.verify(
    signature, # a assinatura gerada no passo anterior
    mensagem, # a mensagem assinada
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ), # o mesmo padding usado no passo anterior
    hashes.SHA256() # o mesmo agoritmo de hashing usado no passo anterior
  )
  print('assinatura válida')
  with open('hash.txt', 'w') as f:
    f.write(signature.hex())
except InvalidSignature:
  print('nn é autentico')