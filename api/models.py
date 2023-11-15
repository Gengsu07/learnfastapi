from database import Base
from sqlalchemy import REAL, Column, Date, Integer, Text


class MPN(Base):
    __tablename__ = "ppmpkm"
    index = Column(Integer, index=True, primary_key=True)
    datebayar = Column(Date)
    kdmap = Column(Text)
    kdbayar = Column(Text)
    nm_kategori = Column(Text)
    kd_kategori = Column(Text)
    nominal = Column(REAL)
