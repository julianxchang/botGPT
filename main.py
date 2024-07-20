from openai import OpenAI
import discord
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
#Ensure the API keys are loaded correctly
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")

groq_client = Groq()

def response(message):
    completion = groq_client.chat.completions.create(
        messages=[
            {"role": "user", 
             "content": message,
             }
        ],
        model="llama3-8b-8192"
    )
    return completion.choices[0].message.content

async def send_message(message, response):
    await message.channel.send(response)

def run_bot():
    TOKEN = DISCORD_API_KEY
    intents = discord.Intents.default()
    intents.message_content = True
    client  = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        user_message = str(message.content)
        if user_message[0] == "?":
            await send_message(message, response(user_message[1:]))
    client.run(TOKEN)

run_bot()