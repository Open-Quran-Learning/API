from ayat import app, base_url
import requests
from flask import request, Response

############################
# ----Helper functions---- #
############################


def send_message(text, chat_id):

    # prepare telegram api link
    url = f'{base_url}sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    # send message to the user
    send = requests.post(url, json=payload)
    if send.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    else:
        return 'baaaaaka'

############################
# ----Telegram Routes---- #
############################


@app.route("/telegram_bot", methods=['POST', 'GET'])
def example0():
    if request.method == 'POST':
        msg = request.get_json()
        text = 'welcome'
        chat_id = msg['message']['chat']['id']
        print(msg)
        send_message(text, chat_id)
        return Response('OK', status=200)
    else:
        return "<h1>Ayat project: Bot<h1>"



@app.route("/")
def index():
    text = request.args.get('text')
    chat_id = request.args.get('chat_id')
    send = send_message(text, chat_id)
    return send