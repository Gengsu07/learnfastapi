from database import Base
from sqlalchemy import Column, Date, Float, Integer, MetaData, String

metadata = MetaData()


class MPN(Base):
    __tablename__ = "ppmpkm"
    index = Column(Integer, index=True, primary_key=True)
    DATEBAYAR = Column(Date)
    KDMAP = Column(String)
    KDBAYAR = Column(String)
    NM_KATEGORI = Column(String)
    KD_KATEGORI = Column(String)
    NOMINAL = Column(Float)
