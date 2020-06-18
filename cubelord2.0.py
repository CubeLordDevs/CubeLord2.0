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
    embed = discord.Embed(
    colour = discord.Colour.green(),
    title = "Ping-Pong Latency Test",
    )
    embed.add_field(name="Results:", value= f'Pong! ```Latency: {round(client.latency * 1000)} milliseconds``` ')
    await ctx.send(embed=embed)

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

    embed = discord.Embed(
    colour=discord.Colour.green(),
    title="8Ball",
    )
    embed.add_field(name="Question:", value=f'{question}')
    embed.add_field(name="Answer:", value=f'{random.choice(responses)}')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/719228435716636842/722661845101576202/pool-8-ball-emoji-clipart-md.png')
    await ctx.send(embed=embed)

# Moderation commands listed below.

# Number 0: Return an error message if one arises. 
@client.event
async def on_command_error(ctx, error):

    # take care of a missing argument in a command
    if isinstance(error, commands.MissingRequiredArgument):

        embed = discord.Embed (
           colour= discord.Colour.dark_red(),
           title= "Error"
        )
        embed.add_field(name="Exception:", value="Invalid command syntax: Please provide all arguments required.")
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/719228435716636842/722802579641335858/matt-icons_dialog-error.png")
        await ctx.send(embed=embed)

    # take care of an invalid command
    if isinstance(error, commands.CommandNotFound):

        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title="Error"
        )
        embed.add_field(name="Exception:", value="Invalid command: This command does not exist.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/719228435716636842/722802579641335858/matt-icons_dialog-error.png")
        await ctx.send(embed=embed)

    # take care of missing permissions
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title="Error"
        )
        embed.add_field(name="Exception:", value="Missing permissions: You do not have permission to do this.")
        embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/719228435716636842/722802579641335858/matt-icons_dialog-error.png")
        await ctx.send(embed=embed)


# Number 1: Kick command (+kick <user> <reason>)
@client.command()
@has_permissions(manage_roles=True, kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Kick Successful!"
    )
    embed.add_field(name="Results:", value=f'User {member.mention} has been kicked due to: {reason}.')
    await member.kick(reason=reason)
    await ctx.send(embed=embed)

# Number 2: Ban command (+ban <user> <reason>)
@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Ban Successful!"
    )
    await member.ban(reason=reason)
    embed.add_field(name="Results:", value=f"User {member.mention} has been banned due to: {reason}.")
    await ctx.send(embed=embed)

# Number 3: Unban command (+unban <user> <reason)
@client.command()
async def unban(ctx, *, member):

    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            embed = discord.Embed(
                colour=discord.Colour.green(),
                title="Ban Successful!"
            )
            await ctx.guild.unban(user)
            embed.add_field(name="Results", value="f'{user.mention} has been unbanned.'")
            await ctx.send(embed=embed)


# Number 4: Find userID of user
@client.command()
async def userid(ctx, user: discord.User):
    id = user.id

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title=f"{user.display_name}'s User ID"
    )
    embed.add_field(name=f"ID: ", value=f"{str(user)}'s User ID is: **{id}**.")
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

# Number 5: Display avatar of mentioned user
@client.command()
async def avatar(ctx, user: discord.User):
    avatar = user.avatar_url

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title=f"Avatar Lookup"
    )
    embed.add_field(name=f"{user.display_name}'s Avatar", value=f"This is {user.display_name}'s Avatar:")
    embed.set_image(url=avatar)
    await ctx.send(embed=embed)

# Run the bot.
# Note: Store token in external file later for security reasons
client.run('NzE5NzQyNDEyMTg4MDI0OTU0.XubgEw.Ub79PYYmYGDVVVhQKqhdA7hNq3U')



