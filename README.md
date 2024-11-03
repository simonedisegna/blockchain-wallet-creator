# Blockchain Wallet Creator

## Descrição
Este projeto consiste em dois scripts para a criação e verificação de carteiras na rede Stellar.
- **create_wallet.py**: Gera um novo par de chaves (pública e privada) e salva em um arquivo JSON.
- **verificar_saldo.py**: Verifica o saldo de uma conta Stellar utilizando a chave pública fornecida.

## Requisitos
Para rodar este projeto, é necessário instalar:
- Python 3.x
- [stellar-sdk](https://pypi.org/project/stellar-sdk/)
- requests

Para instalar as dependências, execute o seguinte comando:
```sh
pip install stellar-sdk requests
```

## Como Usar
### Criar uma Carteira Stellar
1. Execute o script `create_wallet.py` para gerar uma nova carteira Stellar:
   ```sh
   python create_wallet.py
   ```
2. O script gerará uma chave pública e uma chave privada, e salvará ambas no arquivo `stellar_wallet.json`.

### Verificar o Saldo de uma Conta Stellar
1. Abra o arquivo `verificar_saldo.py` e substitua `INCLUIR_CHAVE_PUBLICA` pela chave pública da sua conta Stellar.
2. Execute o script para consultar o saldo:
   ```sh
   python verificar_saldo.py
   ```
3. O script fará uma consulta na Horizon API (testnet) e exibirá os saldos da conta fornecida.

## Estrutura dos Scripts
- **create_wallet.py**: Responsável por gerar um par de chaves Stellar e salvar em um arquivo JSON.
- **verificar_saldo.py**: Consulta o saldo de uma conta Stellar por meio da Horizon API, utilizando a chave pública fornecida.

## Observações
- Os scripts utilizam a **testnet** da Stellar. Para usar na **mainnet**, altere a URL da API para `https://horizon.stellar.org`.
- A chave privada é sensível e não deve ser compartilhada publicamente.
- Após criar as chaves, é necessário validá-las na rede Stellar.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

