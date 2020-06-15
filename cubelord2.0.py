# Import Python packages
import random

# Import discord and create client.
import discord 
from discord.ext import commands
client = commands.Bot(command_prefix = '+')

# Ensure bot is running.
@client.event
async def on_ready():
    print('Ready!')

# Ping-pong command.
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ``` Latency: {round(client.latency * 1000)} milliseconds ``` ')


# Entertainment commands listed below.

# Number 1: 8 Ball Command.
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    # Responses for the bot.
    responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
            ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Run the bot.
client.run('NzE5NzQyNDEyMTg4MDI0OTU0.XubgEw.Ub79PYYmYGDVVVhQKqhdA7hNq3U')
