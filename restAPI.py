import requests
from flask import Flask, jsonify, request
from logic import Translate, languages_list

app = Flask(__name__)


@app.route('/languages', methods=['GET'])
def get_lang_list():
    return jsonify(languages_list)


@app.route('/translate', methods=['GET', 'POST'])
def translate_web_request():
    if request.method == 'GET':
        return jsonify('Введи фразу для перевода в формате json')
    else:
        example = Translate()
        json_msg = request.get_json()
        if len(json_msg) > 1:
            msg_text = json_msg['text']
            example.src_lang = json_msg['src_lang']
            example.dest_lang = json_msg['dest_lang']
            return example.translate_msg(msg_text).text
        else:
            msg_text = json_msg['text']
            return example.translate_msg(msg_text).text


if __name__ == '__main__':
    app.run(debug=True)
