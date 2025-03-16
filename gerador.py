# Criador de senhas seguras com Python
# Autor: Azor T 
import random 
import secrets

receive_number = int(input('Digite o tamanho da senha: '))
Number = random.randint(1, 100)

print(secrets.token_bytes(receive_number))
print(secrets.token_hex(receive_number))
print(secrets.token_urlsafe(receive_number))
print(secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_+'))