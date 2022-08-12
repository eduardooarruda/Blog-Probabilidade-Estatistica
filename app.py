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

@app.route("/coeficiente-variacao")
def coeficiente_variacao():
    return render_template("coeficiente_variacao.html")

@app.route("/media")
def media():
    return render_template("media.html")

@app.route("/mediana")
def mediana():
    return render_template("mediana.html")

@app.route("/moda")
def moda():
    return render_template("moda.html")