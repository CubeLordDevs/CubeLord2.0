# Import Python packages
import random

# Import discord and create client.
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix='+')


# Ensure bot is running and set its status.
@client.event
async def on_ready():
    print('Ready!')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('+'))


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

# Number 0: Return an error message if one arises. 
@client.event
async def on_command_error(ctx, error):

    # take care of a missing argument in a command
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Invalid command syntax: Please provide all arguments required.")
    
    # take care of an invalid command
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command: This command does not exist.")

    # take care of missing permissions
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Missing permissions: You do not have permission to do this.")


# Number 1: Kick command (+kick <user> <reason>)
@client.command()
@has_permissions(manage_roles=True, kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f'User {member.mention} has been kicked due to: {reason}.')
    await member.kick(reason=reason)

# Number 2: Ban command (+ban <user> <reason>)
@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"User {member.mention} has been banned due to: {reason}.")

# Number 3: Find userID of user
@client.command()
async def userid(ctx, user: discord.User):
    id = user.id
    await ctx.send(f"{str(user)}'s User ID is: {id}.")

# Run the bot.
# Note: Store token in external file later for security reasons
client.run('NzE5NzQyNDEyMTg4MDI0OTU0.XubgEw.Ub79PYYmYGDVVVhQKqhdA7hNq3U')
