import math


def codigo_de_golomb(posicao, deslocamento):
    '''
    Código de Golomb, responsável comprimir images,
    utilizado para substituir o código de Huffman.
    '''

    k = int(math.log(deslocamento, 2))
    c = int(math.pow(2, k) - deslocamento)
    r = int(math.fmod(posicao, deslocamento))

    if (r >= 0 and r < c):
        st = "0" + str(k-1) + "b"
        rb = str(format(r, st))  
    else:
        st = "0" + str(k) + "b"
        rb = str(format(r+c, st))
    
    return ("1" * int(posicao / deslocamento)) + "0" + rb