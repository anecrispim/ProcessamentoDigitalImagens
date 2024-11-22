# -*- coding: utf-8 -*-
"""06) PGM8bitsParaPGMbinario.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MG_WO1asNHpt7248HJ_bRpnAzSXQU6YM

Sobre o arquivo de Imagem “Entrada.pgm” (8 bits em escala de cinza, 0-255 PGM – P2(ASCII)), gerar arquivo de saída no mesmo formato, porém binarizado, conforme regras a seguir:
III. Limiar = 128, se valorpixel <= limiar := 0 e valorpixel > limiar := 255;
Obs.: nesta atividade existe similaridade com a atividade 2, sendo o arquivo de saída tipo P1 (binário). Entretanto esta atividade terá como saída arquivo do tipo P1 (escala de cinza), no qual o arquivo de saída deve ter somente valores 0 e 255 no seu conteúdo.
"""

import numpy as np
from PIL import Image

imagem = Image.open("Entrada_EscalaCinza.pgm").convert("L")  # Garantindo que está em escala de cinza
imagem_array = np.array(imagem)

# Aplicando a binarização com o limiar de 128
limiar = 128
imagem_binarizada_array = np.where(imagem_array > limiar, 255, 0).astype(np.uint8)

# Salvar a imagem binarizada no formato P2 (PGM)
with open("Saida_binarizada.pgm", "w") as f:
    f.write("P2\n")  # Formato P2 (grayscale)
    f.write(f"{imagem_binarizada_array.shape[1]} {imagem_binarizada_array.shape[0]}\n")  # Largura e altura
    f.write("255\n")  # Valor máximo para escala de cinza é 255
    for linha in imagem_binarizada_array:
        f.write(" ".join(map(str, linha)) + "\n")  # Converte cada linha para texto e escreve no arquivo