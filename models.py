from sqlmodel import SQLModel, Field, Relationship, create_engine
from enum import Enum
from datetime import date


class Banks(Enum):
    NUBANK = "Nubank"
    SANTANDER = "Santander"
    INTER = "Inter"


class Status(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"


class Transactions_Type(Enum):
    ENTRADA = "Entrada"
    SAIDA = "Saida"


class Account(SQLModel, table=True):
    id: int = Field(primary_key=True)
    balance: float
    bank: Banks = Field(default=Banks.NUBANK)
    status: Status = Field(default=Status.ATIVO)


class Bank_Statement(SQLModel, table=True):
    id: int = Field(primary_key=True)
    account_id: int = Field(foreign_key="account.id")
    account: Account = Relationship()
    transaction_type: Transactions_Type = Field(default=Transactions_Type.ENTRADA)
    balance: float
    date: date


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=False)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
