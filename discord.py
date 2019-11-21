import discord
from googlesearch import search

TOKEN = input("Enter the token of bot: ")

client = discord.Client()
recent_history = list()

def query_results(str):
    query = list()
    for j in search(str, tld='co.in', num=10, stop=5, pause=2):
        query.append(j)
    return query

@client.event
async def on_message(message):
    print(message.content)
    if message.content.lower().startswith('hi'):
        await message.channel.send('hey')
    if message.content.lower().startswith('!google '):
        query = (message.content.lower()).split("!google ", 1)
        with open("query_kavya.txt", "a") as write_file:
            write_file.write(query[1].lower() + "\n")
        result = query_results(query[1])
        for j in result:
            await message.channel.send(j)

    if message.content.lower().startswith('!recent '):
        query = (message.content.lower()).split("!recent ", 1)
        search_word = query[1].lower()
        str1 = ""
        with open('query_kavya.txt') as file:
            for line in file:
                line = line.strip()
                if search_word in line:
                    str1 += "found"
                    recent_history.append(line)
        if not str1:
            await message.channel.send("No recent searches found for " + search_word)
        else:
            history = list(set(recent_history))
            await message.channel.send("Recent searches for " + search_word + " are as follows: \n")
            for i in history:
                await message.channel.send(i)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
