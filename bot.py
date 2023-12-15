import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me about currencies!")

async def supported_currencies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Supported currencies: {'https://www.exchangerate-api.com/docs/supported-currencies'}")
async def get_exchange_rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command_args = context.args

    if not command_args or len(command_args) != 2:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide two currency codes.")
        return

    currency_from = command_args[0].upper()
    currency_to = command_args[1].upper()

    api_url = f'https://v6.exchangerate-api.com/v6/1633af94b3408220c649dc82/latest/{currency_from}'

    try:
        response = requests.get(api_url)
        data = response.json()

        # Получаем курсы валют
        rate_from = data['conversion_rates'].get(currency_from)
        rate_to = data['conversion_rates'].get(currency_to)

        if rate_from is not None and rate_to is not None:
            exchange_rate_message = f"The exchange rate from {currency_from} to {currency_to} is {rate_from:.4f}:{rate_to:.4f}"
        else:
            exchange_rate_message = f"Unable to retrieve exchange rates for {currency_from} and {currency_to}"

        await context.bot.send_message(chat_id=update.effective_chat.id, text=exchange_rate_message)

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error: {str(e)}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command_list = [
        '/start - Start the bot',
        '/exchange_rate <from_currency> <to_currency> - Get the exchange rate between two currencies',
        '/supported_currencies - Get a link to the page listing all supported currencies',
        '/help - Show available commands'
    ]
    await context.bot.send_message(chat_id=update.effective_chat.id, text='\n'.join(command_list))

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command. Type /help for a list of available commands.")


if __name__ == '__main__':
    application = ApplicationBuilder().token('6901677310:AAEfN3teVIhoApZKrh9p3SKmWvDcj9qxZ4A').build()

    start_handler = CommandHandler('start', start)
    exchange_rate_handler = CommandHandler('exchange', get_exchange_rate)
    supported_currencies_handler = CommandHandler('support', supported_currencies)
    help_handler = CommandHandler('help', help_command)
    unknown_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_command)

    application.add_handler(start_handler)
    application.add_handler(exchange_rate_handler)
    application.add_handler(supported_currencies_handler)
    application.add_handler(help_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
