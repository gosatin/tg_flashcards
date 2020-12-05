import requests
import configparser


def telegram_bot_sendtext(bot_message, bot_token, bot_chatID):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


config = configparser.ConfigParser()
config.read('bot.properties')

test = telegram_bot_sendtext("Testing Telegram bot", config.get("BotSection", "bot_token"),
                             config.get("BotSection", "bot_chatID"))
print(test)
