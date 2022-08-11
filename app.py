from flask import Flask,  render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/estatistica-descritiva")
def estatisticaDescritiva():
    return render_template("estatisticaDescritiva.html")

@app.route("/glossario")
def glossario():
    return render_template("glossario.html")

@app.route("/amplitude")
def amplitude():
    return render_template("amplitude.html")

@app.route("/variancia")
def variancia():
    return render_template("varianca.html")

@app.route("/desvio-padrao")
def desvio_padrao():
    return render_template("desvio_padrao.html")