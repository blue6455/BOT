import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import asyncio

# Charger le token depuis .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Définition des intents
intents = discord.Intents.default()
intents.message_content = True

# Création du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Liste des salons où envoyer le message
CHANNEL_ID = [
    1423238426194477156,
    1423253196570103910,
    1423254712236376214,
    1423255075538599957,
    1423255403487039590
]

@bot.event
async def on_ready():
    print(f"✅ Le bot {bot.user} est connecté et prêt !")
    send_and_delete_message.start()  # démarrer la tâche automatique

# Tâche qui envoie un message tous les 3 jours et le supprime après 1 seconde
@tasks.loop(hours=72)  # 72h = 3 jours
async def send_and_delete_message():
    for channel_id in CHANNEL_ID:
        channel = bot.get_channel(channel_id)
        if channel:
            try:
                msg = await channel.send("Ceci est un message temporaire ⏳")
                await asyncio.sleep(1)  # attendre 1 seconde
                await msg.delete()
                print(f"🗑️ Message envoyé puis supprimé dans le salon {channel.name}")
            except Exception as e:
                print(f"❌ Erreur lors de l’envoi dans {channel_id} : {e}")
        else:
            print(f"⚠️ Salon introuvable pour ID {channel_id}")

# Commande manuelle pour tester
@bot.command()
async def testmsg(ctx):
    msg = await ctx.send("Message test ⏳")
    await asyncio.sleep(1)
    await msg.delete()

# Lancer le bot
bot.run(TOKEN)
