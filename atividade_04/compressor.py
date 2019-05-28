import argparse

from codificador import codificador
from decodificador import decodificador


if __name__ == "__main__":
    print("Começando...")

    parser=argparse.ArgumentParser(description="Condifica uma imagem.")
    parser.add_argument("imagem", nargs='?', default="images/Lena.jpg")
    parser.add_argument("nome_arquivo", nargs='?', default="images/codificado.ppm")
    args = parser.parse_args()

    codificador(args.imagem, args.nome_arquivo)