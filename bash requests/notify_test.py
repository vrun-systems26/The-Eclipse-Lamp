# notify_test.py
# Test the Telegram notification pipeline
# Run with: python3 notify_test.py
# Make sure you have your bot token and chat ID from BotFather before running
# Prerequisite: pip install requests

import requests

TOKEN = "your_token_here"
CHAT_ID = "your_chat_id_here"

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

print("Sending alert...")
result = send_alert("🚨 Eclipse Lamp: Person detected in the room!")
print("Sent successfully!" if result["ok"] else "Something went wrong")