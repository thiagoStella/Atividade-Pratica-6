import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')


url = "https://randomuser.me/api/"

print("Fazendo requisição à API...")
resposta = requests.get(url)


if resposta.status_code == 200:
    print(f"Status da Resposta: {resposta.status_code} (Sucesso!)")

    dados = resposta.json()
    # print("\n--- Dados JSON Completos (para referência) ---")
    # print(dados) # Linha opcional: descomente para ver todo o JSON bruto
    # print(f"Tipo dos dados JSON: {type(dados)}")

    usuario = dados["results"][0]

    nome_primeiro = usuario["name"]["first"]
    nome_ultimo = usuario["name"]["last"]
    nome_completo = f"{nome_primeiro} {nome_ultimo}"

    email = usuario["email"]

    pais = usuario["location"]["country"]

    print("\n--- Perfil de Usuário Aleatório ---")
    print(f"Nome: {nome_completo}")
    print(f"Email: {email}")
    print(f"País: {pais}")

else:
    print(f"Erro ao acessar a API. Status: {resposta.status_code}")
    print(f"Mensagem de erro: {resposta.text}") 

input("\nPressione Enter para finalizar o programa...")