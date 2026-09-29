from upi import upi_link
def test_link():
    l = upi_link("tejteja023@upi", "Charan Teja", "99.00")
    assert l.startswith("upi://pay?") and "pa=tejteja023" in l and "am=99" in l
def test_flow():
    from fastapi.testclient import TestClient
    from app import app
    c = TestClient(app)
    r = c.post("/orders", json={"vpa": "shop@upi", "name": "Shop", "amount": "49.00"}).json()
    assert "upi://pay?" in r["link"]
    oid = r["id"]
    assert c.get(f"/orders/{oid}").status_code == 200
    assert c.post("/paid", json={"order_id": oid, "utr": "123456789012"}).json()["paid"] is True
    assert c.get("/qr", params={"link": r["link"]}).status_code == 200
