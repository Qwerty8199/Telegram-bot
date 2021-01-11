import requests
import json

TOK = "1282091921:AAGIZySli2IgsR-ZuPwmRnh7yYvZr-g3tfU"


class Telegram_bot:

    def __init__(self):
        self.TOK = TOK
        self.base_url = "https://api.telegram.org/bot{}".format(self.TOK)

    def get_updates(self,offset=None):
        if offset is None:
            url = self.base_url + "/getupdates"
        else:
            url = self.base_url + "/getupdates?offset={}".format(offset+1)
        re = requests.get(url)
        return json.loads(re.content)

    def send_message(self,chat_id,text):
        url = self.base_url + "/sendmessage?chat_id={}&text={}".format(chat_id,text)
        re = requests.get(url)
        print("Message sent")


bot = Telegram_bot()
msg1 = " was sent by "
updates = bot.get_updates()
items = updates["result"]
update_id = items[0]["update_id"]
while True:
    for item in items:
        update_id = item["update_id"]
        username = item["message"]["from"]["username"]
        msg = item["message"]["text"]
        chat_id = item["message"]["chat"]["id"]
        ms = msg + msg1 + username
        bot.send_message(chat_id, ms)
    updates = bot.get_updates(update_id)
    items = updates["result"]
