from datetime import datetime

from pydantic import BaseModel


class MPN_DATA(BaseModel):
    index: int
    DATEBAYAR: datetime
    KDMAP: str
    KDBAYAR: str
    NM_KATEGORI: str
    KD_KATEGORI: str
    NOMINAL: float

    class Config:
        orm_mode = True
