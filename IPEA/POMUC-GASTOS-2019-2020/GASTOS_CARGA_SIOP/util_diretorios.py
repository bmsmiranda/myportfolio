import time
import os


def exibe_conteudo_diretorios(nm_diretorio_raiz_dados: str):
    """ Exibe o conteudo do diretorio raiz dos dados a serem importados.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs: implementar controle de excecao para caso o parametro seja nulo ou vazio.
    """
    lt_diretorios = []
    lt_arquivos = []
    print("\n" + nm_diretorio_raiz_dados)

    for conteudo in os.listdir(nm_diretorio_raiz_dados):
        nm_path = nm_diretorio_raiz_dados + conteudo

        if os.path.isdir(os.path.join(nm_diretorio_raiz_dados, conteudo)):
            lt_diretorios.append(nm_path)
            print("|")
            print("|-- {}".format(conteudo))

            for arquivo in os.listdir(nm_path):
                print("|\t|-- {}".format(arquivo))   

        elif os.path.isfile(os.path.join(nm_diretorio_raiz_dados, conteudo)):
            lt_arquivos.append(nm_path)

    if len(lt_arquivos) > 0:
        print("|")

    for arquivo in lt_arquivos:
        print("|-- {}".format(arquivo))

