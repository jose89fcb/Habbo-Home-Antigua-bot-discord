import discord
from discord.ext import commands
import json
import requests
import time
from PIL import Image, ImageDraw, ImageFont, ImageFile
import io



 
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 

with open("configuracion.json") as f: #Creamos un archivo de configuracion para el bot
    config = json.load(f)
 
@bot.command()
async def habbohome(ctx, habbonombre, *, hotel):

    await ctx.message.delete() #Borramos el comando para no dejar sucio el chat xD
    await ctx.send("Generando Habbo Home Antigua...", delete_after=0)
    time.sleep(3) #Añadimos un tiempo para que sea borrado
 

 


   
    

    ####
    response = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={habbonombre}")
    try:

     idhabbo = response.json()['uniqueId']
    except KeyError:
     idhabbo="❌"
    try:

     identificador = response.json()['uniqueId'].split("-")[-2]
    except KeyError:
        identificador="❌"

    response = requests.get(f"https://www.habbo.{hotel}/extradata/public/users/{idhabbo}/photos")
    try:

     idcreador = response.json()[0]['creator_id']
    except IndexError:
        idcreador="❌"






    
    bandera_dict = {
    "es": "https://i.imgur.com/IplIfNP.png",
    "com.br":  "https://i.imgur.com/YGQlPor.png",
    "nl":"https://i.imgur.com/fC8eIvR.png",
    "de":"https://i.imgur.com/vUgY11U.png",
    "fr":"https://i.imgur.com/CoLWbjf.png",
    "it":"https://i.imgur.com/va1X4j6.png",
    "com":"https://i.imgur.com/D6vwN9n.png",
    "com.tr":"https://i.imgur.com/wtiow4R.png",
    "fi":"https://i.imgur.com/BpQCpVi.png"
    }
    bandera = bandera_dict[str(hotel)]

   

   
    

   
    
    url = f"https://images.habbo.com/web_images/mypages/{identificador}/{idcreador}.png" #url
    
    
    
    r = requests.get(url)
    if  r.status_code ==200:
        imagen = Image.open(io.BytesIO(requests.get(url).content))
        with io.BytesIO() as imagen_binary:
            imagen.save(imagen_binary, 'PNG')
            imagen_binary.seek(0)


           
            

            embed = discord.Embed(title=f"{habbonombre}", url=f"https://habbo.{hotel}/home/{habbonombre}", description=f" Aquí tienes la Habbo Home de `{habbonombre}` de Habbo {hotel.upper()}", color=discord.Colour.random())
            embed.set_image(url=f"attachment://HabboHomeAntigua.png")
            
            embed.set_thumbnail(url="https://images.habbo.com/c_images/album1584/HHOME.png")
            embed.set_footer(text=f"Habbo.{hotel}", icon_url=f"{bandera}")
            embed.set_author(name=f"HABBO HOME",  icon_url=f"{bandera}")
            
            
           

         
            
            await ctx.send(f"Hola, {ctx.author.mention} este es el póster de {habbonombre}",embed=embed,file=discord.File(fp=imagen_binary, filename=f'HabboHomeAntigua.png'))
           
            

    else:
        await ctx.send(f"{habbonombre} no tiene póster ❌")
        



    

   
    
    


    
    






    
    
        
       
        
    

  
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])
