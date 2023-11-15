from typing import List, Optional

import models
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from models import MPN
from schemas import MPN_DATA
from sqlalchemy import select
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

data = [
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "AKTIVITAS PENYEWAAN DAN SEWA GUNA USAHA TANPA HAK OPSI, KETENAGAKERJAAN, AGEN PERJALANAN DAN PENUNJANG USAHA LAINNYA",
        "DATEBAYAR": "2023-03-21",
        "NOMINAL": -808478.0,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "AKTIVITAS PENYEWAAN DAN SEWA GUNA USAHA TANPA HAK OPSI, KETENAGAKERJAAN, AGEN PERJALANAN DAN PENUNJANG USAHA LAINNYA",
        "DATEBAYAR": "2023-07-05",
        "NOMINAL": -1801666.0,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "AKTIVITAS PENYEWAAN DAN SEWA GUNA USAHA TANPA HAK OPSI, KETENAGAKERJAAN, AGEN PERJALANAN DAN PENUNJANG USAHA LAINNYA",
        "DATEBAYAR": "2023-07-20",
        "NOMINAL": -900833.0,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "INDUSTRI PENGOLAHAN",
        "DATEBAYAR": "2023-05-03",
        "NOMINAL": -6050000.0,
    },
]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"hi": "All"}


@app.get("/all")
async def get_post():
    return data


@app.get("/map/{kdmap}")
async def get_post_by_userid(kdmap: str):
    data_kdmap = [x for x in data if x["KDMAP"] == kdmap]
    return data_kdmap


@app.get("/search")
async def get_post_query(
    kdmap: Optional[str] = None,
    kdbayar: Optional[str] = None,
    sektor: Optional[str] = None,
):
    data_queryed = data
    if kdmap:
        data_queryed = [x for x in data_queryed if x.get("KDMAP") == kdmap]

    if kdbayar:
        data_queryed = [x for x in data_queryed if x.get("KDBAYAR") == kdbayar]

    if sektor:
        data_queryed = [x for x in data_queryed if x.get("NM_KATEGORI") == sektor]
    return data_queryed


@app.get("/mpn", response_model=List[MPN_DATA], status_code=200)
async def get_mpn(db: Session = Depends(get_db)):
    statement = select(MPN).limit(10)
    data = db.execute(statement).scalars().all()
    if not data:
        raise HTTPException(status_code=404, detail="Data Tidak Ditemukan")
    return data


@app.get("/kdmap/{kdmap}", response_model=List[MPN_DATA])
async def get_kdmap(kdmap: str, db: Session = Depends(get_db)):
    stmt = select(MPN).where(MPN.kdmap == kdmap)
    data = db.execute(stmt).scalars().all()
    return data


@app.get("/mpn/search", response_model=List[MPN_DATA])
async def search_mpn(
    db: Session = Depends(get_db),
    kdmap: Optional[str] = None,
    kdbayar: Optional[str] = None,
    sektor: Optional[str] = None,
):
    stmt = select(MPN)
    if kdmap:
        stmt = stmt.filter(MPN.kdmap == kdmap)
    if kdbayar:
        stmt = stmt.filter(MPN.kdbayar == kdbayar)
    if sektor:
        stmt = stmt.filter(MPN.kd_kategori == sektor)

    data = db.execute(stmt).scalars().all()
    if not data:
        raise HTTPException(
            status_code=404, detail=f"Data {kdmap ,kdbayar, sektor} Tidak Ditemukan"
        )
    return data
