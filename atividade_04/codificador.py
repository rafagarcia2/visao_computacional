import cv2
import numpy as np
import argparse

from codigo_de_golomb import codigo_de_golomb

def codificador(imagem, arquivo_codificar):
    '''
    Recebe uma imagem e realiza o processo de compressão,
    ao final geral um imguivo codificado da imagem.

    Parameters
    ----------
    imagem : string
        caminho da imagem fornecida.
    arquivo_codificar : string 
        nome do arquivo que vai guardar o 
        resultado da codificação.

    '''

    image = cv2.imread(imagem)
    grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    img_h, img_w, _ = image.shape
    mValue = 256

    # Pegando arquivo para armazenar codificacao
    arquivo = open(arquivo_codificar, 'w')

    arquivo.write(str(codigo_de_golomb(img_h, mValue)) + "\n")
    arquivo.write(str(codigo_de_golomb(img_w, mValue)) + "\n")

    for i in range(img_h):
        for j in range(img_w):
            pixel = grayscaled[i,j]
            count, i , j = count_values_equals(grayscaled, pixel, i, j, img_h, img_w)

            if (count > 1):
                result = codigo_de_golomb((1000 * count + pixel), mValue)
            else: 
                result = strToBinary(codigo_de_golomb(pixel, mValue))

            print (count, i, j)
            arquivo.write(result)
            arquivo.write("\n")

    arquivo.close()


def count_values_equals(img, value, init_i, init_j, size_h, size_w):
    count = 0
    print ("recebi", init_i, init_j)
    for i in range(init_i, size_h):
        for j in range(init_j, size_h):
            if (img[i,j] == value):
                count += 1
            else: 
                return count, i, j
    return count, init_i, init_j

def strToBinary (s):
    bin_conv = [format(int(c), "b") for c in s]
    return ("".join(bin_conv))


if __name__ == "__main__":
    print("Começando...")

    parser=argparse.ArgumentParser(description="Condifica uma imagem.")
    parser.add_argument("imagem", nargs='?', default="images/Lena.jpg")
    parser.add_argument("nome_arquivo", nargs='?', default="images/codificado.ppm")
    args = parser.parse_args()

    codificador(args.imagem, args.nome_arquivo)