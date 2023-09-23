import openai
import discord
import responses


openai.api_key = ""
def response(message):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
    return completion.choices[0].message.content

async def send_message(message, response):
    await message.channel.send(response)

def run_bot():
    TOKEN = 'MTEyMTM1NjA5NTMxNTc3NTU1OA.GkIyEt.v0CCdILC9CkGjtRsOUBJ89KECFjukfZBxi2SbY'
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
