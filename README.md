# Telegram UPI Pay Bot (Unified Payments demo) - Charan Teja
Demo only - generates UPI intent links + QR, tracks orders, manual UTR confirm. No auto-settlement, no secrets in repo.

## Run
```bash
pip install -r requirements.txt
pytest -q
uvicorn app:app --reload
# POST /orders {"vpa":"shop@upi","name":"Shop","amount":"49.00"}
# GET /qr?link=upi://pay?...
```

## Telegram wiring (you do, token never committed)
1. BotFather -> /newbot -> save token in env BOT_TOKEN
2. python-telegram-bot handlers: /start /order /paid call this FastAPI
3. Webhook: setTelegram webhook -> your https /webhook (stub here, add when deploying)

## Compliance
- Demo UPI links only; real PSP/Razorpay/Cashfree needed for auto-capture
- Never store full account numbers; UTR manual verify in demo
```
