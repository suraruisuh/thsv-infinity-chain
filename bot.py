# === Imports ===
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from database.mongodb import db, get_guild_settings
from utils.logger import log_status, log_error

# === Load Environment ===
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"

# === Bot Initialization ===
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# === Cog Extensions ===
initial_extensions = [
    'cogs.brain_count',
    'cogs.math_dice',
    'cogs.twenty_four',
    'cogs.lightning',
    'cogs.pattern',
    'cogs.equilibrium',         
    'cogs.scramble',            
    'cogs.emoji_math',
    'cogs.admin',               # Loads cogs/admin/__init__.py
    'cogs.mystats',
    'cogs.leaderboard',
    'cogs.help',
    'cogs.calculator',
    'cogs.converter',
    'cogs.purge',
    'cogs.command_list',
    'cogs.support_links',
    'cogs.suggestions'
]

# === Setup Hook ===
@bot.event
async def setup_hook():
    for ext in initial_extensions:
        try:
            await bot.load_extension(ext)
            print(f"✅ Loaded extension: {ext}")
            log_status(bot, message=f"✅ Extension loaded: `{ext}`", force_global=True)
        except Exception as e:
            error_msg = f"❌ Failed to load `{ext}`: {e}"
            print(error_msg)
            log_error(bot, message=error_msg, force_global=True)

# === Bot Ready Event ===
@bot.event
async def on_ready():
    online_msg = f"🤖 Bot **{bot.user}** is online and ready."
    print(online_msg)
    log_status(bot, message=f"🟢 {online_msg}", force_global=True)

    # Log config summary from DB
    print("🔍 Guild Game Channels:")
    settings = list(db.guild_settings.find({}))
    for setting in settings:
        guild_id = setting["_id"]
        brain_channel = setting.get("brain_count_channel")
        print(f"• Guild `{guild_id}` — Brain Count: {brain_channel}")

    # Create DB indexes
    db.user_stats.create_index("last_active")
    db.user_stats.create_index([("_id.guild_id", 1), ("_id.user_id", 1)], unique=True)
    print("✅ MongoDB index setup complete.")

    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} slash commands.")
        log_status(bot, message=f"🔁 Synced {len(synced)} slash commands.", force_global=True)
    except Exception as e:
        error_msg = f"❌ Slash sync failed: {e}"
        print(error_msg)
        log_error(bot, message=error_msg, force_global=True)

# === Disconnect/Resume Events ===
@bot.event
async def on_disconnect():
    msg = f"🔴 Bot `{bot.user}` has disconnected from Discord."
    print(msg)
    log_status(bot, message=msg, force_global=True)

@bot.event
async def on_resumed():
    msg = "🔄 Bot connection resumed."
    print(msg)
    log_status(bot, message=msg, force_global=True)

# === Verification Role Button Handler ===
@bot.event
async def on_interaction(interaction: discord.Interaction):
    if not interaction.guild or not interaction.data:
        return
    if interaction.type != discord.InteractionType.component:
        return

    custom_id = interaction.data.get("custom_id", "")
    if not custom_id.startswith("verify_button_"):
        return

    guild_id = interaction.guild.id
    user = interaction.user
    settings = get_guild_settings(guild_id)
    role_id = settings.get("verify_role_id")

    if not role_id:
        await interaction.response.send_message(
            "⚠️ Verification role not set up. Contact an admin.", ephemeral=True
        )
        return

    role = interaction.guild.get_role(role_id)
    if not role:
        await interaction.response.send_message(
            "⚠️ The verification role no longer exists. Contact an admin.", ephemeral=True
        )
        return

    if role in user.roles:
        await interaction.response.send_message("✅ You’re already verified!", ephemeral=True)
        return

    try:
        await user.add_roles(role, reason="User verified via button")
        await interaction.response.send_message(
            f"✅ You have been verified and granted the **{role.name}** role!", ephemeral=True
        )
    except discord.Forbidden:
        await interaction.response.send_message(
            "❌ I don’t have permission to assign the role. Please contact an admin.", ephemeral=True
        )

# === Start Bot ===
bot.run(TOKEN)
