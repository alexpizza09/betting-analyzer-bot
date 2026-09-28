import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
API_URL = f"https://api.telegram.org/bot{TOKEN}"


def send_message(chat_id, text):
    requests.post(
        f"{API_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text,
        },
    )


def main():
    offset = None

    while True:
        response = requests.get(
            f"{API_URL}/getUpdates",
            params={
                "offset": offset,
                "timeout": 30,
            },
            timeout=35,
        )

        data = response.json()

        for update in data.get("result", []):
            offset = update["update_id"] + 1

            message = update.get("message")

            if not message:
                continue

            chat_id = message["chat"]["id"]
            text = message.get("text", "")

            if text == "/start":
                send_message(
                    chat_id,
                    """🤖 BETTING ANALYZER

Bienvenido.

Soy tu analista personal de apuestas deportivas.

🎾 Tenis
⚽ Fútbol
📊 Estadísticas
💰 Bankroll
🔎 Valor esperado

Comandos:

/analizar
/tenis
/futbol
/valor
/bankroll
/stats
/ayuda
""",
                )

            elif text == "/ayuda":
                send_message(
                    chat_id,
                    """📚 COMANDOS

/analizar — Analizar un partido
/tenis — Próximamente
/futbol — Próximamente
/valor — Buscar valor
/bankroll — Ver banca
/stats — Ver estadísticas

Estamos construyendo el sistema paso a paso 🚀
""",
                )

            else:
                send_message(
                    chat_id,
                    "👋 Recibido. Escribe /ayuda para ver los comandos.",
                )


if __name__ == "__main__":
    main()
