import os, sys
import requests, time
from dotenv import load_dotenv


load_dotenv()
TIMEULAR_KEY = os.getenv("TIMEULAR_KEY")
TIMEULAR_SECRET = os.getenv("TIMEULAR_SECRET")

# Get ngrok URL
time.sleep(3)
r = requests.get("http://localhost:4040/api/tunnels")
ngrok_link = r.json()["tunnels"][0]["public_url"]

payload = {"apiKey": TIMEULAR_KEY, "apiSecret": TIMEULAR_SECRET}
r = requests.post("https://api.timeular.com/api/v3/developer/sign-in", json=payload)
BEARER = r.json()["token"]

r = requests.delete(
    "https://api.timeular.com/api/v3/webhooks/subscription",
    headers={"Authorization": "Bearer " + BEARER},
)
print(r.text)

for event in ["trackingStarted", "trackingStopped"]:
    payload = {"target_url": ngrok_link + "/" + event, "event": event}
    r = requests.post(
        "https://api.timeular.com/api/v3/webhooks/subscription",
        json=payload,
        headers={"Authorization": "Bearer " + BEARER},
    )
    print(r.text)
