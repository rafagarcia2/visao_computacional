import numpy as np
import cv2 


def hough_line(img):
    '''
    Aplica a transformada de hough para encontrar retas em uma
    imagem, retornando a matriz, os thetas e rhos.

    Parameters
    ----------
    img : Image
        Imagem com as bordas já encontradas.
    '''
    # Rho and Theta ranges
    thetas = np.deg2rad(np.arange(-90.0, 90.0))
    width, height = img.shape
    diag_len = np.ceil(np.sqrt(width * width + height * height))   # max_dist
    rhos = np.linspace(-diag_len, diag_len, diag_len * 2.0)

    # Cache some resuable values
    cos_t = np.cos(thetas)
    sin_t = np.sin(thetas)
    num_thetas = len(thetas)

    # Hough accumulator array of theta vs rho
    accumulator = np.zeros((2 * int(diag_len), num_thetas), dtype=np.uint64)
    y_idxs, x_idxs = np.nonzero(img)  # (row, col) indexes to edges

    # Vote in the hough accumulator
    for i in range(len(x_idxs)):
        x = x_idxs[i]
        y = y_idxs[i]

    for t_idx in range(num_thetas):
        # Calculate rho. diag_len is added for a positive index
        rho = round(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len
        accumulator[int(rho), t_idx] += 1

    return accumulator, thetas, rhos
 

def detector_retas(imagem, resultado):
    '''
    Encontra as retas presentes em uma imagem.

    Parameters
    ----------
    imagem : string
        caminho da imagem fornecida.
    resultado : string 
        nome do arquivo que vai guardar o 
        resultado do processamento.
    '''
    img = cv2.imread(imagem) 
    image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    edges = cv2.Canny(image, 50, 150,apertureSize = 3) 


    accumulator, thetas, rhos = hough_line(edges)

    # Easiest peak finding based on max votes
    number_votes = 200

    for _ in range(10):
        idx = np.argmax(accumulator)
        if idx >= number_votes:
            r = rhos[int(idx / accumulator.shape[1])]
            theta = thetas[idx % accumulator.shape[1]]
            accumulator[int(idx / accumulator.shape[1]), idx % accumulator.shape[1]] = 0
            print("rho={0:.2f}, theta={1:.0f}".format(r, np.rad2deg(theta)))

            a = np.cos(theta) 
            b = np.sin(theta) 
            x0 = a*r  
            y0 = b*r 
            
            # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
            x1 = int(x0 + 1000*(-b)) 
            y1 = int(y0 + 1000*(a)) 
        
            # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
            x2 = int(x0 - 1000*(-b)) 
            y2 = int(y0 - 1000*(a)) 
            
            cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2) 
        else:
            break

    cv2.imwrite(resultado, img) 

import argparse

if __name__ == "__main__":
    print("Calculando...")

    parser=argparse.ArgumentParser(description="Encontra as retas em uma imagem.")
    parser.add_argument("imagem", nargs='?', default="imagem_retas.jpeg")
    parser.add_argument("resultado", nargs='?', default="resultado.jpeg")
    args = parser.parse_args()

    detector_retas(args.imagem, args.resultado)

    print("Finalizado!")