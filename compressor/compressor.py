import argparse

from codificador import codificador
from decodificador import decodificador


if __name__ == "__main__":
    print("Comprimindo...")

    parser=argparse.ArgumentParser(description="Realiza a compressão de uma imagem.")
    parser.add_argument("imagem", nargs='?', default="images/Lena.jpg")
    parser.add_argument("nome_arquivo", nargs='?', default="images/codificado.bin")
    parser.add_argument("resultado", nargs='?', default="images/codificado.ppm")
    args = parser.parse_args()

    codificador(args.imagem, args.nome_arquivo)

    decodificador(args.nome_arquivo, args.resultado)

    print("Finalizado!")