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

### Deploy locally with `ngrok`

For this you need to have set `TIMEULAR_KEY` and `TIMEULAR_SECRET` in your environment (.env are supported).

You can deploy your setup locally with `ngrok` and `uvicorn` by running:

```bash
./run.sh 8000
```

Replace `8000` by your port.

*Warning:* your `ngrok` integration will only last for 2 hours if you do not create a user account (free plan) on [https://ngrok.com/](https://ngrok.com/) and launch `ngrok authtoken <ngrok token>` beforehand (this has to be done only once).