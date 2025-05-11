from flask import Flask, request, render_template_string
import requests
import math
import os
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

formulario_html = '''
<!doctype html>
<title>Calcular primos</title>
<h2>Ingrese un número:</h2>
<form method="post">
  <input type="number" name="numero" min="2" required>
  <button type="submit">Calcular</button>
</form>
{% if primos %}
<h3>Primos encontrados:</h3>
<p>{{ primos }}</p>
{% endif %}
'''

NUM_WORKERS = int(os.environ.get("WORKER_REPLICAS"))
WORKER_URL = "http://worker:5000/primos"

@app.route('/', methods=['GET', 'POST'])
def calcular_primos():
    primos = []
    if request.method == 'POST':
        try:
            numero = int(request.form['numero'])
        
            step = math.ceil(numero / NUM_WORKERS)
            rangos = [(i, min(i + step - 1, numero)) for i in range(1, numero + 1, step)]


            def consultar_worker(rango):
                params = {'inicio': rango[0], 'fin': rango[1]}
                try:
                    res = requests.get(WORKER_URL, params=params, timeout=5)
                    if res.status_code == 200:
                        return res.json().get("primos", [])
                except:
                    return []
                return []

            with ThreadPoolExecutor() as executor:
                resultados = executor.map(consultar_worker, rangos)

            for lista in resultados:
                primos.extend(lista)

            primos.sort()

        except ValueError:
            primos = ["Error: entrada inválida"]

    return render_template_string(formulario_html, primos=primos)

app.run(host='0.0.0.0', port=5000)