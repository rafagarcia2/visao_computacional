import cv2
from scipy import fftpack
import numpy as np


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

    image = cv2.imread(imagem, 0).astype(int)
    #grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).astype(int)

    # Pegando arquivo para armazenar codificacao
    arquivo = open(arquivo_codificar, 'w')

    content_h = format(image.shape[0], "d")
    content_w = format(image.shape[1], "d")
    arquivo.write(content_h + "\n")
    arquivo.write(content_w + "\n")

    # Comprimindo o conteudo da imagem
    compress = np.array(dct2(image), dtype=int)
    for height in range(image.shape[0]):
        for width in range(image.shape[1]):
            content_line = format(compress[height, width], "d")
            arquivo.write(content_line + "\n")
    
    arquivo.close()

def dct2(img):
    return fftpack.dct( fftpack.dct(img, axis=0, norm='ortho' ), axis=1, norm='ortho' )
