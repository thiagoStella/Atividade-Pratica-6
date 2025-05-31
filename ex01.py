import random
import string

letras = string.ascii_letters
numeros = string.digits
especiais = string.punctuation
combinacao = letras + numeros + especiais


while True:
    try:
        senha = int(input("Qual a quantidade de caracteres deseja para a nova senha? "))
        if senha < 3 or senha > 20:
            print("Os valores devem ser entre 3 e 20 caracteres")
            continue
        break
    except ValueError:
        print("Erro, digite a quantidade de caracteres que d eseja na senha gerada")

senha_gerada = ''
for _ in range(senha):
    aleatorio = random.choice(combinacao)
    senha_gerada += aleatorio

print(f"A senha gerada é: {senha_gerada}")


input("Encerrar o programa?")