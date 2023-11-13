from typing import Optional

from fastapi import FastAPI

from api.models.blog import Post

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
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "KESENIAN, HIBURAN DAN REKREASI",
        "DATEBAYAR": "2023-09-06",
        "NOMINAL": 1.0,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "KONSTRUKSI",
        "DATEBAYAR": "2023-09-01",
        "NOMINAL": -180000.0,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "PENDIDIKAN",
        "DATEBAYAR": "2023-08-25",
        "NOMINAL": -1.0772069e7,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "PENDIDIKAN",
        "DATEBAYAR": "2023-08-30",
        "NOMINAL": -1.0772069e7,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "PENGANGKUTAN DAN PERGUDANGAN",
        "DATEBAYAR": "2023-08-03",
        "NOMINAL": -1.50389e7,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "PERDAGANGAN BESAR DAN ECERAN REPARASI DAN PERAWATAN MOBIL DAN SEPEDA MOTOR",
        "DATEBAYAR": "2023-03-21",
        "NOMINAL": -2446760.0,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "100",
        "NM_KATEGORI": "PERDAGANGAN BESAR DAN ECERAN REPARASI DAN PERAWATAN MOBIL DAN SEPEDA MOTOR",
        "DATEBAYAR": "2023-05-03",
        "NOMINAL": -2.7576543e7,
    },
    {
        "KDMAP": "411111",
        "KDBAYAR": "",
        "NM_KATEGORI": "AKTIVITAS KEUANGAN DAN ASURANSI",
        "DATEBAYAR": "2023-06-13",
        "NOMINAL": -2.3015696e8,
    },
    {
        "KDMAP": "411112",
        "KDBAYAR": "100",
        "NM_KATEGORI": "KESENIAN, HIBURAN DAN REKREASI",
        "DATEBAYAR": "2023-09-06",
        "NOMINAL": 2.0,
    },
    {
        "KDMAP": "411112",
        "KDBAYAR": "100",
        "NM_KATEGORI": "PERDAGANGAN BESAR DAN ECERAN REPARASI DAN PERAWATAN MOBIL DAN SEPEDA MOTOR",
        "DATEBAYAR": "2023-08-05",
        "NOMINAL": 90000.0,
    },
    {
        "KDMAP": "411119",
        "KDBAYAR": "100",
        "NM_KATEGORI": "AKTIVITAS JASA LAINNYA",
        "DATEBAYAR": "2023-02-02",
        "NOMINAL": 37500.0,
    },
    {
        "KDMAP": "411119",
        "KDBAYAR": "100",
        "NM_KATEGORI": "INDUSTRI PENGOLAHAN",
        "DATEBAYAR": "2023-06-26",
        "NOMINAL": 3.1220943e7,
    },
    {
        "KDMAP": "411119",
        "KDBAYAR": "100",
        "NM_KATEGORI": "INDUSTRI PENGOLAHAN",
        "DATEBAYAR": "2023-07-14",
        "NOMINAL": 3.3374075e7,
    },
    {
        "KDMAP": "411119",
        "KDBAYAR": "100",
        "NM_KATEGORI": "INDUSTRI PENGOLAHAN",
        "DATEBAYAR": "2023-08-10",
        "NOMINAL": 1.42875e7,
    },
    {
        "KDMAP": "411119",
        "KDBAYAR": "100",
        "NM_KATEGORI": "INDUSTRI PENGOLAHAN",
        "DATEBAYAR": "2023-09-11",
        "NOMINAL": 1.0990476e7,
    },
    {
        "KDMAP": "411119",
        "KDBAYAR": "100",
        "NM_KATEGORI": "PENDIDIKAN",
        "DATEBAYAR": "2023-09-07",
        "NOMINAL": 461925.0,
    },
]
post = {}


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


@app.post("/blog")
async def create_post(data: Post):
    return {"data": f"post has been created with title: {data.title}"}
