import discord
import os
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home(): return "Bot Aibot nyala"
def run(): app.run(host='0.0.0.0', port=10000)
Thread(target=run).start()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready(): print(f'{client.user} online')

@client.event 
async def on_message(message):
    if message.author == client.user: return
    if message.content.lower() == 'tes':
        await message.channel.send('Gw online nih!')

client.run(os.getenv('TOKEN'))
