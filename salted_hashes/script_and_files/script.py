from argon2 import PasswordHasher
from argon2.exceptions import HashingError
from argon2.exceptions import VerifyMismatchError, InvalidHash, VerificationError

ph = PasswordHasher()

try:
  hash = ph.hash("118210822")
  print(hash) # $argon2id$v=19$m=65536,t=3,p=4$c3mWN6nQd5NeJmu2u/ZNYg$QnU+7Ogt5uabw0KelcMZOMqKJYZDojt7oo5EAdAmwBA
except HashingError as err:
  print(err)

try:
  ph.verify(hash, input("qual a senha? "))
  print("senha correta")

except VerifyMismatchError as err:  # caso a senha esteja errada ele lança uma exceção
  print(err)

except InvalidHash as err:  # caso o hash passado não esteja do padrão esperado pelo algoritmo
  print(err)

except VerificationError as err: # verificação falha por outro motivo
  print(err)