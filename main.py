from flask import Flask
from textblob import TextBlob
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
# Função para rota 'home'
def home():
    return 'Minha primeira API!'


@app.route('/sentimento/<frase>')
def sentimento(frase):
    traducao = GoogleTranslator(source="pt", target="en").translate(frase)
    traducao_blob = TextBlob(traducao)
    polaridade = traducao_blob.sentiment.polarity

    return f'Polairdade: {polaridade}'


app.run(debug=True)




