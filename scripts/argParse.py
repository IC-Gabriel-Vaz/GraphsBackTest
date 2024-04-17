import argparse
from read_txt import read_txt as rt


def argParse():
    parser = argparse.ArgumentParser(description="Script para ler um arquivo de texto.")
    parser.add_argument("arquivo", type=str, help="Caminho do arquivo de texto a ser lido.")
    args = parser.parse_args()

    arquivo = args.arquivo
    try:
        conteudo = rt(arquivo)
        # print("Conteúdo do arquivo:")
        # print(conteudo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")

    return conteudo


if __name__ == '__main__':

    argParse()