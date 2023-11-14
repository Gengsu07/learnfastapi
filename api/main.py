from typing import Optional

from database import get_session
from fastapi import Depends, FastAPI
from models import MPN
from sqlmodel import Session, select

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


@app.get("/mpn", response_model=list[MPN])
async def get_mpn(session: Session = Depends(get_session)):
    statement = select(MPN)
    data = session.exec(statement).all()
    return data
