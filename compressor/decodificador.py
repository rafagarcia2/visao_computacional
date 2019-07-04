import cv2
from scipy import fftpack
import numpy as np


def decodificador(arquivo_codificado, resultado):
    '''
    Recebe uma imagem e realiza o processo de decodificação
    a fim de recuperar a imagem original comprimida.

    Parameters
    ----------
    arquivo_codificado : string 
        caminho do arquivo codificado que será
        decodificado após a compressão.
    resultado : string
        caminho para armazenar a imagem que
        resultará do processo de decodificação.
    '''

    codificado = open(arquivo_codificado, 'r')

    height = int(codificado.readline())
    width = int(codificado.readline())

    # Recuperando a imagem original comprimida
    img = [[int(codificado.readline()) for _ in range(width)] for _ in range(height)]
    imagem = np.array(img, dtype='int64')
    codificado.close()

    # salvando o resultado
    cv2.imwrite(resultado, idct2(imagem))


def idct2(img):
    return fftpack.idct(fftpack.idct(img, axis=0, norm='ortho'), axis=1, norm='ortho')