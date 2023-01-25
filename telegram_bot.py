import requests
import config

def telegram_bot_sendtext(bot_message):

    send_text = 'https://api.telegram.org/bot' + config.token + '/sendMessage?chat_id=' + config.bot_chatID_s + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
