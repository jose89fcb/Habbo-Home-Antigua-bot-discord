import discord
from discord.ext import commands
import json
import requests
import time
from PIL import Image, ImageDraw, ImageFont, ImageFile
import io
import PIL
 
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 

with open("configuracion.json") as f: #Creamos un archivo de configuracion para el bot
    config = json.load(f)
 
@bot.command()
async def habbohome(ctx, *, habboNombre):

    await ctx.message.delete() #Borramos el comando para no dejar sucio el chat xD
    await ctx.send("Generando Habbo Home Antigua...", delete_after=0)
    time.sleep(3) #Añadimos un tiempo para que sea borrado

    ####
    response = requests.get(f"https://www.habbo.es/api/public/users?name={habboNombre}")
    idhabbo = response.json()['uniqueId']
    identificador = response.json()['uniqueId'].split("-")[-2]
    ###
    response = requests.get(f"https://www.habbo.es/extradata/public/users/{idhabbo}/photos")
    try:

     idcreador = response.json()[0]['creator_id']
    except IndexError:
        idcreador="❌"

   

   
    

    
    
   
    
    url = f"https://images.habbo.com/web_images/mypages/{identificador}/{idcreador}.png" #url
    
    
    
    

    imagen = Image.open(io.BytesIO(requests.get(url).content))
    
   
    
    


    
    






    
    with io.BytesIO() as imagen_binary:
       
        
        imagen.save(imagen_binary, 'PNG')
        
        imagen_binary.seek(0)
        
       
        
        await ctx.send(file=discord.File(fp=imagen_binary, filename=f'HabboHomeAntigua.png'))

  
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])