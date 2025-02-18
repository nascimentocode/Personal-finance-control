from models import Account, Banks, Status, Bank_Statement, Transactions_Type, engine

from sqlmodel import Session, select
from datetime import date, timedelta


def create_account(account: Account):
    with Session(engine) as session:
        statement = select(Account).where(Account.bank == account.bank)
        results = session.exec(statement).all()

        if results:
            print("Ja existe uma conta nesse banco!")
            return

        session.add(account)
        session.commit()
        return Account


def list_account():
    with Session(engine) as session:
        statement = select(Account)
        results = session.exec(statement).all()

        return results


def disable_account(id):
    with Session(engine) as session:
        statement = select(Account).where(Account.id == id)
        account = session.exec(statement).first()
        if account.balance > 0:
            raise ValueError("Essa conta ainda possui saldo.")
        if account.status == Status.INATIVO:
            raise ValueError("Essa conta ja esta inativa!")

        account.status = Status.INATIVO
        session.commit()


def transfer_balance(id_account_out, id_account_in, balance):
    with Session(engine) as session:
        statement = select(Account).where(Account.id == id_account_out)
        account_out = session.exec(statement).first()

        if account_out.status == Status.INATIVO:
            raise ValueError(
                "Esta conta está inativa e não deve haver transações envolvendo-a."
            )

        if account_out.balance < balance:
            raise ValueError("Saldo insuficiente.")

        statement = select(Account).where(Account.id == id_account_in)
        account_in = session.exec(statement).first()

        if account_in.status == Status.INATIVO:
            raise ValueError(
                "Esta conta está inativa e não deve haver transações envolvendo-a."
            )

        account_out.balance -= balance
        account_in.balance += balance
        session.commit()


def financial_transaction(bank_statement: Bank_Statement):
    with Session(engine) as session:
        statement = select(Account).where(Account.id == bank_statement.account_id)
        account = session.exec(statement).first()

        if account.status == Status.INATIVO:
            raise ValueError(
                "Esta conta está inativa e não deve haver transações envolvendo-a."
            )

        if bank_statement.transaction_type == Transactions_Type.ENTRADA:
            account.balance += bank_statement.balance
        else:
            if account.balance < bank_statement.balance:
                raise ValueError("Saldo insuficiente!")

            account.balance -= bank_statement.balance

        session.add(bank_statement)
        session.commit()

        return bank_statement


def total_accounts():
    with Session(engine) as session:
        statement = select(Account)
        accounts = session.exec(statement).all()

        total = sum([account.balance for account in accounts])

        return float(total)


def fetch_bank_statement_between_dates(initial_date: date, final_date: date):
    with Session(engine) as session:
        statement = select(Bank_Statement).where(
            Bank_Statement.date >= initial_date, Bank_Statement.date <= final_date
        )

        results = session.exec(statement).all()

        return results


def create_graph_by_account():
    with Session(engine) as session:
        statement = select(Account).where(Account.status == Status.ATIVO)
        accounts = session.exec(statement).all()
        banks = [account.bank.value for account in accounts]
        total = [account.balance for account in accounts]

        import matplotlib.pyplot as plt

        plt.bar(banks, total)
        plt.show()
