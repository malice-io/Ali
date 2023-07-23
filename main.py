import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send("Oi!")
    
    await bot.process_commands(message)
bot.run("MTEzMjQ2MjA3Mzc5MjY5NjMyMA.Gyjdjf.JZSBX1IcNECuEon69fpTlw4ez3Xfjx95Nh4Fx0")
