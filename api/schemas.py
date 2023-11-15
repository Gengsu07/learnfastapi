from datetime import date

from pydantic import BaseModel


class MPN_DATA(BaseModel):
    index: int
    datebayar: date
    kdmap: str
    kdbayar: str
    nm_kategori: str
    kd_kategori: str
    nominal: float

    class Config:
        orm_mode = True
