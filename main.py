import os
import asyncio
import discord
from discord.enums import Status
from dotenv import load_dotenv

from fastapi import FastAPI, Request

app = FastAPI()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(client.start(TOKEN))


@app.post("/trackingStopped")
async def trackingStopped(request: Request):
    # https://developers.timeular.com/#ee43a6cf-0307-4a73-ac2b-71f50feac605
    current_activity = "😴"

    await client.change_presence(
        activity=discord.Activity(
            name=current_activity, type=discord.ActivityType.playing
        )
    )


@app.post("/")
@app.post("/trackingStarted")
async def trackingStarted(request: Request):
    # https://developers.timeular.com/#ee43a6cf-0307-4a73-ac2b-71f50feac605
    payload = await request.json()

    current_activity = "😴"
    try:
        current_activity = payload["data"]["currentTracking"]["activity"]["name"]
    except Exception as e:
        print(e)

    await client.change_presence(
        activity=discord.Activity(
            name=current_activity,
            type=discord.ActivityType.playing,
            status=Status.online,
        )
    )
