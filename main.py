from auth_data import token
import requests
from datetime import datetime
import telebot
from telebot import types

def crypto_bahasy(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    jogap = requests.get(url)
    data = jogap.json()
    shu_gun_sene = datetime.now().strftime("%d.%m.%Y %H:%M")

    if crypto in data:
        return f"{crypto.capitalize()} bahasy: {data[crypto]['usd']}$\nSene: {shu_gun_sene}"
    else:
        return "Bagyslan kriptowalyutan bahasyny owrenip bilmedim"
    
menin_botym = telebot.TeleBot(token)

@menin_botym.message_handler(commands=["start"])
def start_knopka(message):
    if message:
        klawiatura = types.InlineKeyboardMarkup(row_width=2)

        bitcoin_knopka = types.InlineKeyboardButton("Bitcoin bahasy", callback_data="bitcoin")
        litecoin_knopka = types.InlineKeyboardButton("Litecoin bahasy", callback_data="bitcoin")
        ethereum_knopka = types.InlineKeyboardButton("Ethereum bahasy", callback_data="ethereum")

        klawiatura.add(bitcoin_knopka, litecoin_knopka, ethereum_knopka)

        menin_botym.send_message(message.chat.id, "Haysy kripti-walyutan bahasyny owrenesiniz gelyar?", reply_markup=klawiatura)

@menin_botym.callback_query_handler(func = lambda call:True)
def knoplara_basynlada_jogap(callback):
    if callback.message:
        bahasy = crypto_bahasy(callback.data)
        menin_botym.send_message(callback.message.chat.id, f"{bahasy}")
        start_knopka(callback.message)

menin_botym.polling()