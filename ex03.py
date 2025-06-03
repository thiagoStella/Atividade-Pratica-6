import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

cep = input("Digite o Cep : ")
cep_numero = cep.replace("-","").replace(".","").strip()

if len(cep_numero) != 8:
    print("Erro! O CEP deve conter 8 digitos!")
elif not cep_numero.isdigit():
    print("Erro! O CEP deve conter somente números")
else:
    print(f"CEP válido para consulta: {cep_numero}")

    url_api = f"https://viacep.com.br/ws/{cep_numero}/json/"

    print(f"URL da API a ser consultada: {url_api}")

    resposta = requests.get(url_api)

    print(f"Status da requisição: {resposta.status_code}")

    if resposta.status_code == 200:
        dados = resposta.json()        
        if "erro" in dados and dados["erro"] ==True:
            print(f"CEP '{cep_numero}' não encontrado ou inválido")
        else:        
            logradouro = dados["logradouro"]
            bairro = dados["bairro"]
            cidade = dados["localidade"]
            estado = dados["uf"]
        
            print("- INFORMAÇÕES DO ENDEREÇO -")
            print(f"Logradouro: {logradouro}")
            print(f"Bairro: {bairro}")
            print(f"Cidade: {cidade}")
            print(f"Estado: {estado}")    
            
    else:
        print(f"Erro na consulta à API. Status: {resposta.status_code}")
        print("Verifique sua conexão ou tente novamente mais tarde.")


input("\nPressione Enter para finalizar o programa...")