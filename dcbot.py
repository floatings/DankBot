import discord,main
import wm as weedmaps
from discord.ext import commands


client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

theraleaf = "theraleaf-relief-inc"
whitefire = "white-fire"
elemental = "elementalwellness"
haze = "haze-1"
cal = "caliva"
cacol = "ca-collective"
mary = "mary-joe-10"
plpc = "purple-lotus"
airfield = "airfield-supply-company"
guild = "guild"




@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

char = ['a','b','c','d']


searchkeys = []
dispokeys = {
    "whitefire": ['white','fire','whitefire','wf'],
    "caliva":['cal','caliva','ca'],
    "cacollective":['ccol', 'caco', 'cacol', 'cac','cacoll', 'cacollective','collective', 'cc'],
    "maryjoe":['mary','joe','maryjoe','maryandjoe','mj','mandj','mary&joe'],
    "plpc":['purple','purp','lotus','pl','plpc','purplelotus'],
    "airfield":['af','airfield','air','field','afs','airfieldsupply'],
    "theraleaf":['thera','tl','theraleaf','th'],
    "guild":['theguild','urbanleaf','urban','urbn','ul','tg','gld'],
    "elemental":['elemental','wellness','elementalwellness','elem','ele','ew']

}
@client.command(pass_context=True)
async def w(ctx, *args):
    out = ''
    res = ()
    if(len(args)<1):
        msg = 'Invalid arguments! See **.w help**'
        await ctx.send(msg)
    elif args[0].strip().lower() in dispokeys['theraleaf']:
        res = weedmaps.scrape(theraleaf, args[1])
    elif args[0].strip().lower() in dispokeys['whitefire']:
        res = weedmaps.scrape(whitefire, args[1])
    elif args[0].strip().lower() in dispokeys['elemental']:
        res = weedmaps.scrape(elemental, args[1])
    elif "haze" in args[0].strip():
        res = weedmaps.scrape(haze, args[1])
    elif args[0].strip().lower() in dispokeys['caliva']:
        res = weedmaps.scrape(cal, args[1])
    elif args[0].strip().lower() in dispokeys['cacollective']:
        res = weedmaps.scrape(cacol, args[1])
    elif args[0].strip().lower() in dispokeys['maryjoe']:
        res = weedmaps.scrape(mary, args[1], "deliveries")
    elif args[0].strip().lower() in dispokeys['plpc']:
        res = weedmaps.scrape(plpc, args[1])
    elif args[0].strip().lower() in dispokeys['airfield']:
        res = weedmaps.scrape(airfield, args[1])
    elif args[0].strip().lower() in dispokeys['guild']:
        res = weedmaps.scrape(guild, args[1])
    elif "help" in args[0].strip():
        disp = ''
        for store in dispokeys:
            disp += str(store) + " " + str(dispokeys[store]) + "\n"
        msg = '**Usage:**\n.w <store> <category>\n' \
              '**Stores:**\ntheraleaf, whitefire, elemental, haze, ca collective, mary & joe, purple lotus, airfield, urbanleaf\n**Categories:** \n(V) vape, (C/W) wax, ' \
              '(F/T) tree, (E) edibles\n**Dictionary:**\n' + disp
        await ctx.send(msg)
    else:
        msg = 'Command not found. See **.w help**'
        await ctx.send(msg)


    i = 0
    if(res):
        for word in res[0]:
            if (i < 10):
                out += word + "\n"
                i=i+1
    if out:
        title = res[2].title() + " / " +  res[1].title()
        found = str(len(res[0])) + " results found"
        embedVar = discord.Embed(title=title, description=found, color=0x355A20)
        embedVar.add_field(name="Price: Low to High", value=out.title(), inline=False)
        ping = "{} Search Completed".format(ctx.message.author.mention) + " For: " + res[2].title() + " " + res[1].title() +  " " +res[3]
        await ctx.send(ping)
        react1 = "➡"
        react2 ="⬅"
        sent = await ctx.send(embed=embedVar)
        await sent.add_reaction(emoji=react2)
        await sent.add_reaction(emoji=react1)


@client.event
async def on_reaction_add(reaction, user):
    for role in user.roles:
        # administrator role name = 'test_role'
        if role.name == 'test_role':
            break
    else:
        i = 0
        if reaction.emoji == "⬅" and reaction.count > 1:
            print (i)
            i = i+1
            print("left")
            await reaction.remove(user)
            channel = client.get_channel(817483405767344189)
            print("www:", channel, type(channel))
            id = reaction.message.id
            print(id)
            message = await channel.fetch_message(id)
            print("wwwwwwww: " + str(type(message)))
            embed = discord.Embed.to_dict(message.embeds[0])
            #embed2 = discord.Embed.title(message.embeds[0])
            print(embed)
            print("danames: ", embed['fields'][0]['value'])
            prevproducts = embed['fields'][0]['value']
            print("www:", embed['title'])
            key = embed['title'].replace(' ','')
            prodarr = prevproducts.split("\n")
            keylen = int(prodarr[-1][:2])
            actlen = len(prodarr)
            print("lenkey", keylen)
            vars = key.split("/")
            print(vars)
            res = weedmaps.scrape(vars[0].lower(),vars[1].lower())
            i = keylen - (actlen*2)
            out = ''
            arrlen = str(len(res[0])) + " results found"
            print('act', actlen)
            if (res):
                for word in res[0][i:]:
                    if (i < keylen-10):
                        out += word + "\n"
                        print("word: ", word)
                        i = i + 1

                editedBed = discord.Embed(title=embed['title'], description=arrlen, color=0x355A20)
                editedBed.add_field(name="Price: Low to High",
                                   value=out.title(), inline=False)


            await reaction.message.edit(embed=editedBed)
            pass
            pass
        elif reaction.emoji == "➡" and reaction.count > 1:
            print (i)
            i = i+1
            print("left")
            await reaction.remove(user)
            channel = client.get_channel(817483405767344189)
            print("www:", channel, type(channel))
            id = reaction.message.id
            print(id)
            message = await channel.fetch_message(id)
            print("wwwwwwww: " + str(type(message)))
            embed = discord.Embed.to_dict(message.embeds[0])
            #embed2 = discord.Embed.title(message.embeds[0])
            print(embed)
            print("danames: ", embed['fields'][0]['value'])
            prevproducts = embed['fields'][0]['value']
            print("www:", embed['title'])
            key = embed['title'].replace(' ','')
            prodarr = prevproducts.split("\n")
            keylen = int(prodarr[-1][:2])
            print("lenkey", keylen)
            vars = key.split("/")
            print(vars)
            res = weedmaps.scrape(vars[0].lower(),vars[1].lower())
            i = keylen
            out = ''
            arrlen = str(len(res[0])) + " results found"
            if (res):
                for word in res[0][keylen:]:
                    if (i < keylen+10):
                        out += word + "\n"
                        print("word: ", word)
                        i = i + 1

                editedBed = discord.Embed(title=embed['title'], description=arrlen, color=0x355A20)
                editedBed.add_field(name="Results Found",
                                   value=out.title(), inline=False)


            await reaction.message.edit(embed=editedBed)
            pass

@client.command(pass_context=True)
async def s(ctx, *args):
    subreddit = args[0]
    out = ''

    if (subreddit=='a'):
        embedVar = discord.Embed(title= "/r/Aquaswap Search", color=0xFF5700)
        scrape = main.webauth(main.auth, main.data, main.headers, args[0])
        res = main.searchposts(scrape, main.keywords_a)
        print(res)
        for found in res:
            out += found + "\n"
        length = str(len(res)) + " Results Found"
        embedVar.add_field(name=length, value=out,inline=False)
        sent = await ctx.send(embed=embedVar)
    elif (subreddit=='b'):

        scrape = main.webauth(main.auth, main.data, main.headers, args[0])
        res = main.searchposts(scrape, main.keywords_b)
        print(res)
        for found in res:
            out += found + "\n"
        length = str(len(res)) + " Results Found"
        embedVar = discord.Embed(title= "/r/Mechmarket Search", color=0xFF5700)
        embedVar.add_field(name=length, value=out,inline=False)
        sent = await ctx.send(embed=embedVar)




client.run('key')
