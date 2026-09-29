from urllib.parse import urlencode
def upi_link(pa: str, pn: str, am: str, cu: str = "INR", tn: str = "Telegram order") -> str:
    assert "@" in pa, "VPA must contain @"
    q = urlencode({"pa": pa, "pn": pn, "am": am, "cu": cu, "tn": tn})
    return f"upi://pay?{q}"

def order_msg(order_id: str, amount: str, link: str) -> str:
    return (f"Order {order_id} - Rs.{amount}\nPay via UPI app (GPay/PhonePe/Paytm):\n{link}\n"
            f"After paying, send /paid {order_id} with UTR to confirm (demo - manual verify, no auto-settlement).")
