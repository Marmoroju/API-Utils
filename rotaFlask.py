from flask import Flask

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return "Ola, Mundo!"

@app.route("/status", methods=["GET"])
def status():
    return "Servidor ativo e rodando!"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)

