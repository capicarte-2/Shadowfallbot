import discord
from discord import app_commands
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)
tree = app_commands.CommandTree(client)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Shadowfall está vivo no Fly.io!"

def run_web():
    app.run(host="0.0.0.0", port=3000)

Thread(target=run_web).start()

@client.event
async def on_ready():
    await tree.sync()
    print(f"✅ {client.user} conectado!")

# Comandos Slash com resposta ephemeral
@tree.command(name="ping", description="Veja a latência do bot.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"🏓 Pong! {round(client.latency * 1000)}ms", ephemeral=True)

@tree.command(name="help", description="Veja todos os comandos do Shadowfall.")
async def help_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**📜 Comandos disponíveis:**\n"
        "`/ping` - Latência do bot.\n"
        "`/status` - Status do jogador.\n"
        "`/time` - Ver seu time.\n"
        "`/spawn` - Voltar ao ponto inicial.\n"
        "`/missao` - Pega uma missão aleatória.\n"
        "`/ilha` - Lista as ilhas de Shadowfall.\n"
        "`/capivara` - ???\n"
        "`/lucasmig` - ???\n"
        "`/shadowcapi` - ???\n"
        "`/sabedoria` - Receba uma frase épica.\n"
        "`/atributo` - Veja ou evolua seus atributos.\n"
        "`/historia` - História do Shadowfall.\n"
        , ephemeral=True
    )

@tree.command(name="status", description="Mostra seus atributos.")
async def status(interaction: discord.Interaction):
    await interaction.response.send_message("🛡️ Status: Espada: 10 | Vida: 20 | Magia: 5 | Stamina: 8", ephemeral=True)

@tree.command(name="time", description="Mostra seu time atual.")
async def time(interaction: discord.Interaction):
    await interaction.response.send_message("⚔️ Você está no time **Capivara**!", ephemeral=True)

@tree.command(name="spawn", description="Voltar ao ponto inicial.")
async def spawn(interaction: discord.Interaction):
    await interaction.response.send_message("🌍 Você foi teleportado ao ponto de início.", ephemeral=True)

@tree.command(name="missao", description="Receba uma missão aleatória.")
async def missao(interaction: discord.Interaction):
    await interaction.response.send_message("🎯 Missão: Derrote 5 NPCs sombrios!", ephemeral=True)

@tree.command(name="ilha", description="Veja todas as ilhas disponíveis.")
async def ilha(interaction: discord.Interaction):
    await interaction.response.send_message("🏝️ Ilhas: Capivari, Arcania, Vulkarion, Umbra, Celestia", ephemeral=True)

@tree.command(name="capivara", description="Descubra o segredo da Capivara.")
async def capivara(interaction: discord.Interaction):
    await interaction.response.send_message("🦫 A Capivara é a guardiã da primeira ilha!", ephemeral=True)

@tree.command(name="lucasmig", description="Descubra quem é Lucasmig.")
async def lucasmig(interaction: discord.Interaction):
    await interaction.response.send_message("🏹 Lucasmig é o mestre da magia e arqueiro lendário!", ephemeral=True)

@tree.command(name="shadowcapi", description="Descubra quem é o Shadow Capi.")
async def shadowcapi(interaction: discord.Interaction):
    await interaction.response.send_message("🌑 Shadow Capi controla o destino entre Luz e Sombra!", ephemeral=True)

@tree.command(name="sabedoria", description="Receba uma frase sábia.")
async def sabedoria(interaction: discord.Interaction):
    await interaction.response.send_message("🧠 *'A sombra não existe sem a luz.'*", ephemeral=True)

@tree.command(name="atributo", description="Veja ou evolua seus atributos.")
async def atributo(interaction: discord.Interaction):
    await interaction.response.send_message("📊 Atributos: Espada: 15 | Vida: 12 | Stamina: 9 | (Evolução infinita!)", ephemeral=True)

@tree.command(name="historia", description="Descubra a lore de Shadowfall.")
async def historia(interaction: discord.Interaction):
    await interaction.response.send_message(
        "📖 Shadowfall é um mundo dividido entre a Luz e a Sombra.\n"
        "Você deve escolher seu caminho e lutar por seu legado nas ilhas lendárias...",
        ephemeral=True
    )

client.run(os.environ["DISCORD_TOKEN"])