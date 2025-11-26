import os
import datetime as dt
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]  # keep as string

ROTOWIRE_LINEUPS_URL = "https://www.rotowire.com/basketball/nba-lineups.php"

def build_message() -> str:
    today = dt.datetime.now().strftime("%A, %b %d, %Y")
    text = (
        f"NBA projected starting lineups for {today}:\n"
        f"{ROTOWIRE_LINEUPS_URL}\n\n"
        "Source: RotoWire NBA Starting Lineups."
    )
    return text

def send_telegram_message(text: str) -> None:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "disable_web_page_preview": False,
    }
    resp = requests.post(url, json=payload, timeout=15)
    resp.raise_for_status()

def main():
    msg = build_message()
    send_telegram_message(msg)

if __name__ == "__main__":
    main()
