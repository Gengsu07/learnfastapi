from datetime import datetime

from sqlmodel import Date, Field, SQLModel


class MPN(SQLModel, table=True):
    index: int = Field(primary_key=True)
    DATEBAYAR: datetime = Field(Date)
    KDBAYAR: str = Field(nullable=True)
    NM_KATEGORI: str = Field(nullable=True)
    KD_KATEGORI: str = Field(nullable=True)
    NOMINAL: float
