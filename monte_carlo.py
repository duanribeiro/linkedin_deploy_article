import random
import math
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/monte_carlo')
def monte_carlo():
  dentro_circulo = 0
  total_tentativas = request.args.get('tentativas')   # Número total de tentativas
  total_tentativas = int(total_tentativas)  # Tranformando de "texto" para "número"

  for tentativa in range(total_tentativas):
    # Vou gerar uma cordenada aleatória dentro do quadrado
    x2 = random.random() ** 2
    y2 = random.random() ** 2

    # Se a cordenada estiver dentro do círculo eu vou contar
    if math.sqrt(x2 + y2) < 1.0:
        dentro_circulo += 1

  pi = (dentro_circulo / total_tentativas) * 4

  return jsonify(pi)


if __name__ == "__main__":
    app.run()