# timeular-discord-integration

This is a minimalistic timeular discord integration that will change the satus of a bot according to which activity is currently tracked by timeular. It is implemented using FastAPI.

## Getting started

You need to set the `DISCORD_TOKEN` with your discord app token. You can use a .env file.

```bash
git clone https://github.com/tcosmo/timeular-discord-integration.git
cd timeular-discord-integration.git
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Deploying locally

You can deploy your setup locally with `ngrok`, replace `8000` by the port you are using in `uvicorn`:

```bash
ngrok http 8000
```

Then, register timeular events `trackingStarted` and `trackingStopped` on `/trackingStarted` and `/trackingStopped` of your `ngrox` URL:

```bash
curl --location --request POST 'https://api.timeular.com/api/v3/developer/sign-in' \
--header 'Content-Type: application/json' \
--data-raw '{
  "apiKey"    : "{{TIMEULAR_API_KEY}}",
  "apiSecret" : "{{TIMEULAR_API_SECRET}}"
}'
```

```bash
curl --location --request POST 'https://api.timeular.com/api/v3/webhooks/subscription' \
--header 'Authorization: Bearer <AUTH_TOKEN>' \
--data-raw '{
    "event": "trackingStarted",
    "target_url": "https://your-url/trackingStarted"
}'
```

```bash
curl --location --request POST 'https://api.timeular.com/api/v3/webhooks/subscription' \
--header 'Authorization: Bearer <AUTH_TOKEN>' \
--data-raw '{
    "event": "trackingStopped",
    "target_url": "https://your-url/trackingStopped"
}'
```

And you're good to go :) 

Useful links:

- [https://developers.timeular.com/#ee43a6cf-0307-4a73-ac2b-71f50feac605](https://developers.timeular.com/#ee43a6cf-0307-4a73-ac2b-71f50feac605)
- [https://discord.com/developers/applications](https://discord.com/developers/applications)

