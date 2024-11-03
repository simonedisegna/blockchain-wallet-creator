import json
from stellar_sdk import Keypair

# Gera um novo par de chaves (chave pública e chave privada)
keypair = Keypair.random()

# Extrai as chaves geradas
public_key = keypair.public_key
secret_key = keypair.secret

# Salva as chaves em um arquivo JSON
wallet_data = {
    "public_key": public_key,
    "secret_key": secret_key
}

with open("stellar_wallet.json", "w") as wallet_file:
    json.dump(wallet_data, wallet_file)

print(f"Carteira Stellar criada e salva em 'stellar_wallet.json'.")
print(f"Chave Pública: {public_key}")
print(f"Chave Privada: {secret_key}")
