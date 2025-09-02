from flask import Flask, request, jsonify
from textblob import TextBlob
from deep_translator import GoogleTranslator
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('casas.csv')

colunas = ['tamanho', 'ano', 'garagem']

X = df.drop('preco', axis=1)
y = df['preco']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)


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

@app.route('/cotacao/', methods=['POST'])
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco_estimado = modelo.predict([dados_input])

    return jsonify(preco_estimado=preco_estimado[0])


app.run(debug=True)




