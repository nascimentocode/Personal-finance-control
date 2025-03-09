# Controle de Finanças Pessoais

Um projeto de controle de finanças pessoais via terminal, desenvolvido em Python puro, utilizando a arquitetura MVT (Model-View-Template).
Este projeto foi desenvolvido durante a imersão "4 Days 4 Projects - Edição 2" da Pythonando.

## Funcionalidades

- Criar conta bancária
- Desativar conta bancária
- Transferir dinheiro entre contas
- Realizar transações bancárias
- Visualizar o total de saldo entre as contas
- Consultar extrato em um período de datas
- Gerar um gráfico do saldo de cada conta

## Tecnologias Utilizadas

- Python 3.x
- Matplotlib (para geração de gráficos)
- SQLite (para armazenamento de dados)

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/nascimentocode/Personal-finance-control.git
   ```
   Ou, se preferir clonar com chave SSH:
   ```sh
   git clone git@github.com:nascimentocode/Personal-finance-control.git
   ```
2. Navegue ate o projeto
   ```sh
   cd Personal-finance-control
   ```
3. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
5. Execute o programa:
   ```sh
   python templates.py
   ```

## Como Usar

1. Escolha uma opção no menu principal.
2. Siga as instruções para realizar a operação desejada.
3. Consulte extratos e gere relatórios conforme necessário.

## Estrutura do Projeto (MVT)

```
controle-financas/
├── models/     
├── views/  
├── templates/
├── database/
└── requirements.txt
```

## Exemplo de Uso

```sh
Bem-vindo ao Controle de Finanças Pessoais!
Escolha uma opção:
1 - Criar Conta Bancária
2 - Desativar Conta
3 - Transferir Dinheiro
4 - Realizar Transação
5 - Ver Saldo Total
6 - Consultar Extrato
7 - Gerar Gráfico de Saldos
8 - Sair
```

## Contribuição

Sinta-se à vontade para contribuir com o projeto! Basta seguir os passos:

1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade ou correção.
3. Envie um pull request com suas alterações.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
