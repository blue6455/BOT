import discord
import os
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")

CHANNEL_ID = [
    1423238426194477156,
    1423253196570103910,
    1423254712236376214,
    1423255075538599957,
    1423255403487039590
]

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"✅ Connecté en tant que {self.user}")
        for channel_id in CHANNEL_ID:
            channel = self.get_channel(channel_id)
            if channel:
                try:
                    msg = await channel.send("Message temporaire ⏳")
                    await asyncio.sleep(1)
                    await msg.delete()
                    print(f"🗑️ Message supprimé dans {channel.name}")
                except Exception as e:
                    print(f"❌ Erreur dans {channel_id} : {e}")
            else:
                print(f"⚠️ Salon introuvable : {channel_id}")
        await self.close()

client = MyClient(intents=intents)
client.run(TOKEN)