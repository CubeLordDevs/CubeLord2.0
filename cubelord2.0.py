# Import Python packages
import random

# Import discord and create client.
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

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


# Moderation commands listed below.

# Number 2: Kick command (+kick <user> <reason>)
@client.command()
@has_permissions(manage_roles=True, kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
        await ctx.send(f'User {member.display_name} has been kicked due to: {reason}')
        await member.kick(reason=reason)

# Number 3: Ban command (+ban <user> <reason>)
@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"User {member.display_name} has been banned due to: {reason}")

# Run the bot.
client.run('NzE5NzQyNDEyMTg4MDI0OTU0.XubgEw.Ub79PYYmYGDVVVhQKqhdA7hNq3U')

