from flask import Flask, request, jsonify

app = Flask(__name__)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

@app.route('/primos')
def calcular_rango():
    inicio = int(request.args.get('inicio', 1))
    fin = int(request.args.get('fin', 1))
    primos = [n for n in range(inicio, fin + 1) if es_primo(n)]
    return jsonify({"primos": primos})

app.run(host='0.0.0.0', port=5000)
