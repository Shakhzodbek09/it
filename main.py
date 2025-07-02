import os
import telebot
from telebot.types import ReplyKeyboardMarkup

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Environment variable BOT_TOKEN is not set")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

def main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🤖 IT Darslar")
    kb.row("📕 Ingliz Tili Darslari", "📚 Matematika Darslari")
    kb.add("✉️ Biz bilan bog'lanish")
    kb.row("⚙️ Tugmalar muharriri", "📝 Xabarlar muharriri")
    return kb

def it_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🌐Web Dasturlash", "🌐Web Dizayn")
    kb.row("💻Kompyuter Savodxonligi", "🎨Grafik Dizayn")
    kb.row("📊SMM va Marketing", "📙3D Modellashtirish")
    kb.row("🛡Kiber Xavfsizlik", "📱 Android Dasturlash")
    kb.row("🔗Suniy Intellekt", "📼Video Mantaj")
    kb.row("🎲Motion Grafik", "📱Mobilografiya")
    kb.row("🔙 Orqaga", "🔝 Asosiy Menyu")
    return kb

@bot.message_handler(commands=['start'])
def handle_start(message):
    first_name = message.from_user.first_name or "do'st"
    greeting = (
        f"👋 Assalom-u alaykum {first_name}!\n\n"
        "🤖 <b>IT Talim</b> botiga xush kelibsiz!\n"
        "Quyidagi bo'limlardan birini tanlab, zamonaviy darslarni <b>bepul</b> o'rganishni boshlang!"
    )
    bot.send_message(message.chat.id, greeting, reply_markup=main_menu())

@bot.message_handler(func=lambda _: True)
def handle_menu(message):
    txt = message.text

    if txt == "🤖 IT Darslar":
        bot.send_message(message.chat.id, "🤖 IT Darslar bo'limi", reply_markup=it_menu())
        return

    if txt in {
        "📕 Ingliz Tili Darslari",
        "📚 Matematika Darslari",
        "🌐Web Dasturlash",
        "🌐Web Dizayn",
        "💻Kompyuter Savodxonligi",
        "🎨Grafik Dizayn",
        "📊SMM va Marketing",
        "📙3D Modellashtirish",
        "🛡Kiber Xavfsizlik",
        "📱 Android Dasturlash",
        "🔗Suniy Intellekt",
        "📼Video Mantaj",
        "🎲Motion Grafik",
        "📱Mobilografiya",
    }:
        bot.send_message(message.chat.id, "⚠️ Afsuski, bu bo'lim hali <b>tugatilmagan</b>.")
        return

    if txt == "✉️ Biz bilan bog'lanish":
        contact = (
            "📨 <b>Biz bilan bog'lanish</b>\n\n"
            "👨‍💻 Bot yaratuvchisi — Shohzod Farhodov\n"
            "📬 Murojaatlar uchun — @N1Coders"
        )
        bot.send_message(message.chat.id, contact, disable_web_page_preview=True)
        return

    if txt == "🔙 Orqaga":
        bot.send_message(message.chat.id, "🔙 Siz asosiy ro'yxatga qaytdingiz", reply_markup=main_menu())
        return

    if txt == "🔝 Asosiy Menyu":
        bot.send_message(message.chat.id, "🏠 Asosiy menyu", reply_markup=main_menu())
        return

    bot.send_message(message.chat.id, "🤔 Iltimos, menyudagi tugmalardan birini tanlang.", reply_markup=main_menu())

if __name__ == "__main__":
    print("[+] Bot started – polling Telegram for updates…")
    bot.infinity_polling(skip_pending=True)
