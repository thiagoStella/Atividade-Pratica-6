import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=== COTAÇÃO DE MOEDAS ===")
print("Digite USD, para Dolar americano")
print("Digite EUR, para Euro")
print("Digite, GBP,para Libra")
print("=========================")
moeda = input("Informe a moeda a ser cotada: ")
moeda = moeda.upper().strip()

url_api = None

if moeda == 'USD':
    url_api = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
elif moeda == 'EUR':
    url_api = 'https://economia.awesomeapi.com.br/json/last/EUR-BRL'
elif moeda == 'GBP':
    url_api = 'https://economia.awesomeapi.com.br/json/last/GBP-BRL'
else:
    print("Código inválido")

if url_api:
    print(f"Consulta sendo realizada em: {url_api}")

    try:
        resposta = requests.get(url_api, timeout=10)
        print(f"Status da requisição {resposta.status_code}")

        if resposta.status_code == 200:
            dados = resposta.json()

            if not dados:
                print(f"Não foi possivel cotar a moeda {moeda}. Verifique o código")
            else:
                moeda_retornada = list(dados.keys())[0] # pega o primeiro indice de chave
                cotacao = dados[moeda_retornada]

                valor_atual = float(cotacao['bid'])
                valor_maximo = float(cotacao['high'])
                valor_minimo = float(cotacao['low'])

                data_hora_str = cotacao['create_date']
                
                print("\n--- Cotação Atual ---")
                print(f"Moeda: {cotacao['name']} ({moeda}/BRL)")
                print(f"Valor Atual (Compra): R$ {valor_atual:.2f}")
                print(f"Valor Máximo (24h): R$ {valor_maximo:.2f}")
                print(f"Valor Mínimo (24h): R$ {valor_minimo:.2f}")
                print(f"Última Atualização: {data_hora_str}")

        else:
            print(f"Erro na consulta à API. Status: {resposta.status_code}")
            print("Pode haver um problema no servidor da API ou na sua requisição.")



    except requests.exceptions.ConnectionError:
        print("Erro de conexão: Não foi possível conectar à API. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("Erro de tempo limite: A API demorou muito para responder.")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro inesperado ao fazer a requisição: {e}")
    except Exception as e:
        print(f"Ocorreu um erro ao processar os dados da cotação: {e}")

input("\nPressione Enter para finalizar o programa...")