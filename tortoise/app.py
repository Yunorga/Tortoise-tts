# from flask import Flask, render_template, request

# app = Flask(__name__)
# app.static_folder = 'static'
    

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/action', methods=['POST'])
# def action():
#     # Récupérez les données envoyées par le client (par exemple, un message)
#     message = request.form.get('message')
    
#     # Effectuez l'action souhaitée (par exemple, imprimer le message côté serveur)
#     print(f"Message reçu du client : {message}")
    
#     # Vous pouvez également renvoyer une réponse au client si nécessaire
#     return 'Action réussie !'

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
from flask_socketio import SocketIO

print("Start load tortoise")
# from gen import gen
print("End of the load of tortoise")

import argostranslate.package
import argostranslate.translate

from_code = "fr"
to_code = "en"

app = Flask(__name__)
app.static_folder = 'static'

app.config['SECRET_KEY'] = 'my_secret_key'
socketio = SocketIO(app)

voices = ["Donald","Joe","Barack","Elizabeth","Elon","Bruce Wayne"]
# voices = ["trump","biden","obama","queen","elon","batman"]

@app.route('/')
def index():
    return render_template('index.html')
    

@socketio.on('message')
def on_message(message):
    print("message2 : ",message)
    socketio.emit('results', ["audio/trump.mp3","audio/segment_1.wav","../results/generated_trump.wav"])
    # socketio.emit('message', message)

@socketio.on('start')
def on_start():
    print("start : ")
    socketio.emit('voices', voices)

@socketio.on('gen')
def on_gen(data):
    print("gen : ")
    print(data)
    text, voice, trad = data

    # if user requested a trad we need to process the text before gen
    if (trad) :
        text = argostranslate.translate.translate(text, from_code, to_code)

    print(text)
    # paths = gen(text,voice)
    # socketio.emit('result', paths)

if __name__ == '__main__':
    socketio.run(app,debug=True,port=3333)
