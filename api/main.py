from typing import Optional

from fastapi import FastAPI

from api.data import get_data
from api.models.blog import PostIn

app = FastAPI()

data = get_data()
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
async def create_post(
    data: PostIn,
):
    return {"data": f"post has been created with title: {data.title}"}
