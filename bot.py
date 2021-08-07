import discord
import os
import random

client = discord.Client()

@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event

async def on_message(message):
    if message.author == client.user:
        return



    ''''
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    '''
    
    if message.content.startswith('$role1'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 1")
      print("Added",var,"for",member)
      await member.add_roles(var)
    
    if message.content.startswith('$role-1'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 1")
      print("Removed",var,"for",member)
      await member.remove_roles(var)

    if message.content.startswith('$role2'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 2")
      print("Added",var,"for",member)
      await member.add_roles(var)
    
    if message.content.startswith('$role-2'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 2")
      print("Removed",var,"for",member)
      await member.remove_roles(var)

    if message.content.startswith('$role3'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 3")
      print("Added",var,"for",member)
      await member.add_roles(var)
    
    if message.content.startswith('$role-3'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 3")
      print("Removed",var,"for",member)
      await member.remove_roles(var)
    
    if message.content.startswith('$role4'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 4")
      print("Added",var,"for",member)
      await member.add_roles(var)
    
    if message.content.startswith('$role-4'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 4")
      print("Removed",var,"for",member)
      await member.remove_roles(var)
    
    if message.content.startswith('$role5'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 5")
      print("Added",var,"for",member)
      await member.add_roles(var)
    
    if message.content.startswith('$role-5'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 5")
      print("Removed",var,"for",member)
      await member.remove_roles(var)
    
    if message.content.startswith('$role6'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 6")
      print("Added",var,"for",member)
      await member.add_roles(var)
    
    if message.content.startswith('$role-6'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 6")
      print("Removed",var,"for",member)
      await member.remove_roles(var)
    
    if message.content.startswith('$role7'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 7")
      print("Added",var,"for",member)
      await member.add_roles(var)
    
    if message.content.startswith('$role-7'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 7")
      print("Removed",var,"for",member)
      await member.remove_roles(var)
    
    if message.content.startswith('$role8'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 8")
      print("Added",var,"for",member)
      await member.add_roles(var)
    
    if message.content.startswith('$role-8'):
      member = message.author
      var = discord.utils.get(message.guild.roles, name = "Role 8")
      print("Removed",var,"for",member)
      await member.remove_roles(var)

    if message.content.startswith('roll the dice'):

      await message.channel.send('You rolled: '+str(random.randint(0,6)))


client.run('ODUzODc0Mzk4'+'ODUxND'+'k4MDA0.Y'+'MbugA.jJwWYFnWS4pC7'+'ZBAuJwfC'+'h_cUu8')
