# Gerador 2.0 - Gerador de senhas aleatórias com IA. 
# Aqui você vai poder ter diferentes tipos de senhas, com diferentes tamanhos e complexidades.

import random 
import string
import secrets

# Função para perguntar qual tipo de senha o usuario deseja
tipo = input("Qual tipo de senha você deseja? (Fácil, Médio, Difícil, Personalizado): ")
tamanho = int(input('Qual o tamanho da senha? '))

# Função para gerar senha fácil
def senha_facil(tamanho):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(secrets.choice(caracteres) for i in range(tamanho))
    return senha

# Função para gerar senha médio 
def senha_medio(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for i in range(tamanho))
    return senha

# Função para gerar senha difícil
def senha_dificil(tamanho):
    if tamanho < 4:
        print('Senha muito curta para gerar no modo díficil! ')

    senha = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase), 
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha += [secrets.choice(caracteres) for i in range(tamanho - 4)]
    random.shuffle(senha)
    return ''.join(senha)

# Função escolher o tipo da senha que vai ser gerado
def escolher_senha(tipo, tamanho):
    if tipo in ['Fácil', 'fácil', 'facil', 'Facil', 'f', 'F']:
        return senha_facil(tamanho)
    elif tipo in ['Médio', 'médio', 'medio', 'Medio', 'm', 'M']:
        return senha_medio(tamanho)
    elif tipo in ['Difícil', 'difícil', 'dificil', 'Dificil', 'd', 'D']:
        return senha_dificil(tamanho)
    else:
        print('Tipo de senha inválido!')

# Gerar/Mostrar senha na tela
senha = escolher_senha(tipo, tamanho)
print(f'Sua senha gerada foi: {senha}')
