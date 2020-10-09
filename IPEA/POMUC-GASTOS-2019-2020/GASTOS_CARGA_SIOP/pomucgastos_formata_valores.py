import pomucgastos_constantes as pgcst


def formata_nm_arquivo_importacao(nm_arquivo_dados: str):
    """ Texto.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs:
    """
    if nm_arquivo_dados != None and nm_arquivo_dados != "":
        return nm_arquivo_dados[nm_arquivo_dados.find(pgcst.NM_PREFIXO_ARQUIVO) : -1]
    else:
        return ""

