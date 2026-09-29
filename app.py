from fastapi import FastAPI
from pydantic import BaseModel
from upi import upi_link, order_msg
from qrutil import qr_png_bytes
from fastapi.responses import Response
import itertools
app = FastAPI(title="Telegram UPI Pay Bot backend - Charan Teja")
_orders = {}
_id = itertools.count(1001)
class NewOrder(BaseModel):
    vpa: str
    name: str
    amount: str
    note: str = "Telegram order"
@app.get("/")
def root(): return {"status": "ok", "note": "set BOT_TOKEN env, webhook Telegram -> /webhook (stub), demo UPI links only"}
@app.post("/orders")
def new(o: NewOrder):
    oid = f"ORD{next(_id)}"
    link = upi_link(o.vpa, o.name, o.amount, tn=o.note)
    _orders[oid] = {"id": oid, "amount": o.amount, "link": link, "paid": False, "utr": None}
    return {"id": oid, "link": link, "message": order_msg(oid, o.amount, link)}
@app.get("/orders/{oid}")
def get(oid: str): return _orders.get(oid, {"error": "not found"})
@app.get("/qr")
def qr(link: str):
    return Response(content=qr_png_bytes(link), media_type="image/png")
class Paid(BaseModel):
    order_id: str
    utr: str
@app.post("/paid")
def paid(p: Paid):
    if p.order_id not in _orders:
        return {"error": "not found"}
    _orders[p.order_id].update({"paid": True, "utr": p.utr})
    return _orders[p.order_id]
