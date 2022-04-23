import discord 
import os
import asyncio
my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
        .format(client))
start = 1
counter = 0
if start == 1:
  counter += 1
  
async def susu_task():
    await client.wait_until_ready() # ensures cache is loaded
    susu_ping = "Susu kar lo @here"
    channel_general = client.get_channel(871964199453098065)
    while not client.is_closed():
      await channel_general.send(susu_ping)
      await asyncio.sleep(1800)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.loop.create_task(susu_task()) # best to put it in here

client.run(my_secret)