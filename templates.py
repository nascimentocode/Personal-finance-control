from models import *
from views import *

from datetime import datetime


class UI:
    def start(self):
        while True:
            print(
                """
            [1] -> Criar conta
            [2] -> Desativar conta
            [3] -> Transferir dinheiro
            [4] -> Movimentar dinheiro
            [5] -> Total de saldo nas contas
            [6] -> Filtrar extrato por data
            [7] -> Gráfico
                """
            )

            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self._create_account()
            elif choice == 2:
                self._disable_account()
            elif choice == 3:
                self._transfer_balance()
            elif choice == 4:
                self._financial_transaction()
            elif choice == 5:
                self._total_accounts()
            elif choice == 6:
                self._fetch_bank_statement_between_dates()
            elif choice == 7:
                self._create_graph()
            else:
                break

    def _create_account(self):
        print("Digite o nome de algum dos bancos abaixo:")
        for bank in Banks:
            print(f"---{bank.value}---")

        bank = input().title()
        balance = float(input("Digite o valor atual disponível na conta: "))

        account = Account(bank=Banks(bank), balance=balance)
        create_account(account)

    def _disable_account(self):
        print("Escolha a conta que deseja desativar.")
        for account in list_account():
            if account.balance == 0:
                print(f"{account.id} -> {account.bank.value} -> R$ {account.balance}")

        id_account = int(input())

        try:
            disable_account(id_account)
            print("Conta desativada com sucesso.")
        except ValueError as e:
            print(e)

    def _transfer_balance(self):
        print("Escolha a conta que deseja retirar dinheiro.")
        for account in list_account():
            print(f"{account.id} -> {account.bank.value} -> R$ {account.balance}")

        account_out_id = int(input())

        print("Escolha a conta que deseja enviar dinheiro.")
        for account in list_account():
            if account.id != account_out_id:
                print(f"{account.id} -> {account.bank.value} -> R$ {account.balance}")

        account_in_id = int(input())

        balance = float(input("Digite o valor para transferir: "))
        try:
            transfer_balance(account_out_id, account_in_id, balance)
        except ValueError as e:
            print(e)

    def _financial_transaction(self):
        print("Escolha a conta.")
        for account in list_account():
            print(f"{account.id} -> {account.bank.value} -> R$ {account.balance}")

        account_id = int(input())

        balance = float(input("Digite o valor movimentado: "))

        print("Selecione o tipo da movimentação")
        for transaction_type in Transactions_Type:
            print(f"---{transaction_type.value}---")

        transaction_type = input().title()
        bank_statement = Bank_Statement(
            account_id=account_id,
            transaction_type=Transactions_Type(transaction_type),
            balance=balance,
            date=date.today(),
        )
        financial_transaction(bank_statement)

    def _total_accounts(self):
        print(f"R$ {total_accounts()}")

    def _fetch_bank_statement_between_dates(self):
        initial_date = input("Digite a data de início: ")
        final_date = input("Digite a data final: ")

        initial_date = datetime.strptime(initial_date, "%d/%m/%Y").date()
        final_date = datetime.strptime(final_date, "%d/%m/%Y").date()

        for bank_statement in fetch_bank_statement_between_dates(
            initial_date, final_date
        ):
            print(f"{bank_statement.balance} - {bank_statement.transaction_type.value}")

    def _create_graph(self):
        create_graph_by_account()


UI().start()
