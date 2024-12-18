# -*- coding: utf-8 -*-
"""Atividade 4)  Converter PGM 8bits em 5 bits.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1554jUofbxkY8TVovNwGt0LN875UnDDt7

Converter de Imagem “Entrada.pgm” (8 bits escala de cinza, 0-255) em 5 bits de intensidade.
Obs. Lembre que 8 bits quer dizer que os valores variam de 0 a 255, e 5 bits os valores variam de 0 a 31, ou seja precisa ser desenvolvido um fator de conversão.
"""

import numpy as np
from PIL import Image

# Abrindo a imagem em escala de cinza
imagem = Image.open("Entrada_EscalaCinza.pgm")
imagem_array = np.array(imagem)

fator_conversao = 31 / 255

# Aplicando o fator de conversão e arredondar os valores
imagem_5bits_array = np.round(imagem_array * fator_conversao).astype(np.uint8)

# Salvando a nova imagem em escala de 5 bits
imagem_5bits = Image.fromarray(imagem_5bits_array)
imagem_5bits.save("Saida_5bits.pgm")