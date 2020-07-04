# Import Python packages
import random

# Import discord and create client.
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

# Import Discord-Reddit library
import praw

# import secretStuff.py file
import secretStuff

# Initialize Reddit hook.
reddit = praw.Reddit(client_id=secretStuff.secretStuff["client_id"],
                     client_secret=secretStuff.secretStuff["client_secret"],
                     user_agent=secretStuff.secretStuff["user_agent"])
# Set prefix.
client = commands.Bot(command_prefix='+')

# Ensure bot is running and set its status.
@client.event
async def on_ready():
    print('Ready!')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('+help/+info'))

# Miscellaneous commands and events listed below.

# Miscellaneous Command #1: Ping Pong Latency Test Command (!ping).
@client.command()
async def ping(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Ping-Pong Latency Test",
    )
    embed.add_field(name="Results:", value=f'**Pong! ```Latency: {round(client.latency * 1000)} milliseconds```**')
    embed.set_footer(text=f"CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                     icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

# Miscellaneous Event #2: Error Messages.

@client.event
async def on_command_error(ctx, error):
    # "MissingRequiredArgument" exception error message.
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title="Error"
        )
        embed.add_field(name="Exception:", value=f"**Invalid command syntax: Please provide all arguments required.**")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/719228435716636842/722802579641335858/matt-icons_dialog-error"
                ".png")
        embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                         icon_url=client.user.avatar_url)

        await ctx.send(embed=embed)

    # "CommandNotFound" exception error message.
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title="Error"
        )
        embed.add_field(name="Exception:", value=f"**Invalid command: This command does not exist.**")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/719228435716636842/722802579641335858/matt-icons_dialog-error"
                ".png")
        embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                         icon_url=client.user.avatar_url)

        await ctx.send(embed=embed)

    # "MissingPermission" exception error message.
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            colour=discord.Colour.dark_red(),
            title="Error"
        )
        embed.add_field(name="Exception:", value=f"**Missing permissions: You do not have permission to do this.**")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/719228435716636842/722802579641335858/matt-icons_dialog-error"
                ".png")
        embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                         icon_url=client.user.avatar_url)

        await ctx.send(embed=embed)

# Miscellaneous Command #3: Info Command (+info).
@client.command()
async def info(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="About CubeLord2.0"
    )
    embed.add_field(name="Description:",
                    value=f"CubeLord2.0 is a 50/50 moderation/entertainment bot created by using discord.py! To see the bot's commands, type **+help**.")
    embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                     icon_url=client.user.avatar_url)
    embed.set_thumbnail(url=client.user.avatar_url)

    await ctx.send(embed=embed)

# Entertainment commands listed below.

# Entertainment Command #1: 8 Ball Command (!8ball <question>).
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
    embed.add_field(name="Question:", value=f'**{question}**')
    embed.add_field(name="Answer:", value=f'**{random.choice(responses)}**')
    embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                     icon_url=client.user.avatar_url)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/719228435716636842/722661845101576202/pool-8-ball-emoji-clipart'
            '-md.png')

    await ctx.send(embed=embed)

# Entertainment Command #2: Fun Fact Command (+funfact)
@client.command()
async def funfact(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Here's A Fun Fact!"
    )

    facts = [

        "The scientific term for brain freeze is “sphenopalatine ganglioneuralgia!”",
        "Canadians say “sorry” so much that a law was passed in 2009 declaring that an apology can’t be used as evidence of admission to guilt!",
        "Back when dinosaurs existed, there used to be volcanoes that were erupting on the moon!",
        "The only letter that doesn’t appear on the periodic table is J!",
        "If a Polar Bear and a Grizzly Bear mate, their offspring is called a “Pizzy Bear”!",
        "In 2006, a Coca-Cola employee offered to sell Coca-Cola secrets to Pepsi. Pepsi responded by notifying Coca-Cola!",

    ]

    embed.add_field(name="Did you know that...", value=f'**{random.choice(facts)}**')
    embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                     icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

# Entertainment Command #3: Find Memes (using Reddit webhook) (<+meme> <subreddit name>)
@client.command()
async def meme(ctx, sr):
    memes_submissions = reddit.subreddit(sr).hot()
    post_to_pick = random.randint(1, 100)

    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    if submission.over_18:
        embed = discord.Embed(

            colour=discord.Colour.green(),
            title="Notice"
        )
        embed.add_field(name="Description:", value="This submission is NSFW. Please get a meme from another subreddit.")
        embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                         icon_url=client.user.avatar_url)

        await ctx.send(embed=embed)

    elif not submission.over_18:
        embed = discord.Embed(
            colour=discord.Colour.green(),
            title=submission.title
        )

        embed.add_field(name=f"Author:", value=f"**{str(submission.author)}**")
        embed.set_image(url=submission.url)
        embed.add_field(name="From:", value=f"**r/{str(submission.subreddit)}**")
        embed.add_field(name="Upvotes:", value=f"**{str(submission.score)}**")
        embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                         icon_url=client.user.avatar_url)

        await ctx.send(embed=embed)

# Entertainment Command #4: Rock-Paper-Scissors Game (<+rps> <choice>)

@client.command()
async def rps(ctx, userChoice):

    botChoices = ["rock", "paper", "scissors"]
    botChoice = botChoices[random.randint(0,2)]

    async def win():
        embed = discord.Embed(
            colour=discord.Colour.green(),
            title="You Won! :("
        )
        embed.add_field(name="Result:",
                        value=f"**{ctx.message.author.mention}** beat CubeLord2.0! **({str(userChoice)} vs {str(botChoice)})**")

        await ctx.send(embed=embed)

    async def loss():
        embed = discord.Embed(
            colour=discord.Colour.red(),
            title="You Lost! :)"
        )
        embed.add_field(name="Result:",
                        value=f"CubeLord2.0 beat **{ctx.message.author.mention}**! **({str(botChoice)} vs {str(userChoice)})**")

        await ctx.send(embed=embed)

    async def tie():
        embed = discord.Embed(
            colour=discord.Colour.darker_grey(),
            title="It's a Tie!"
        )
        embed.add_field(name="Result:",
                        value=f"Both **{ctx.message.author.mention}** and **CubeLord2.0** played **{str(botChoice)}**.")

        await ctx.send(embed=embed)

    if botChoice == userChoice:
        await tie()
    elif userChoice == "rock":
        if botChoice == "paper":
            await loss()
        else:
            await win()
    elif userChoice == "paper":
        if botChoice == "scissors":
            await loss()
        else:
            await win()
    elif userChoice == "scissors":
        if botChoice == "rock":
            await loss()
        else:
            await win()

# Moderation commands listed below.

# Moderation Command #1: Kick Command (+kick <user> <reason>).
@client.command()
@has_permissions(manage_roles=True, kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Kick Successful!"
    )
    embed.add_field(name="Results:", value=f'**User {member.mention} has been kicked due to: {reason}.**')
    embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                     icon_url=client.user.avatar_url)

    await member.kick(reason=reason)
    await ctx.send(embed=embed)

# Moderation Command #2: Ban Command (+ban <user> <reason>).
@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Ban Successful!"
    )
    embed.add_field(name="Results:", value=f"**User {member.mention} has been banned due to: {reason}.**")
    embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                     icon_url=client.user.avatar_url)

    await member.ban(reason=reason)
    await ctx.send(embed=embed)


# Moderation Command #3: Unban Command (+unban <user>).
@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            embed = discord.Embed(
                colour=discord.Colour.green(),
                title="Unban Successful!"
            )
            embed.add_field(name="Results", value=f'**User{user.mention} has been unbanned.**')
            embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                             icon_url=client.user.avatar_url)

            await ctx.guild.unban(user)
            await ctx.send(embed=embed)


# Moderation Command #4: Find UserID Command (+userid <user>).
@client.command()
async def userid(ctx, user: discord.User):
    userID = user.id

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title=f"{user.display_name}'s User ID"
    )
    embed.add_field(name=f"ID: ", value=f"{user.mention}'s User ID is: **{userID}**.")
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                     icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)


# Moderation Command #5: Display Avatar Command (+avatar <user>).
@client.command()
async def avatar(ctx, user: discord.User):
    avatar = user.avatar_url
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title=f"Avatar Lookup"
    )
    embed.add_field(name=f"Avatar:", value=f"**This is {user.mention}'s Avatar:**")
    embed.set_image(url=avatar)
    embed.set_footer(text="CubeLord2.0: Created by Dodesimo#0176 and Redapple8787#2399.",
                     icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

# Run the bot.
# Note: Store token in external file later for security reasons.
client.run(secretStuff.secretStuff["token"])
