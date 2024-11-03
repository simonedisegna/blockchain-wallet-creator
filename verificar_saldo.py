import requests

# Substitua pela chave pública da sua conta Stellar
public_key = "INCLUIR_CHAVE_PUBLICA"

# URL da Horizon API para consultar a conta na testnet
url = f"https://horizon-testnet.stellar.org/accounts/{public_key}"

# Fazer a solicitação GET para Horizon
response = requests.get(url)

if response.status_code == 200:
    account_data = response.json()
    print("Informações da Conta Stellar:")
    print(f"Chave Pública: {account_data['account_id']}")
    print("Saldos:")
    for balance in account_data['balances']:
        print(f"- Tipo: {balance['asset_type']}, Saldo: {balance['balance']}")
else:
    print(f"Erro ao consultar a conta: {response.status_code}, Detalhes: {response.text}")
