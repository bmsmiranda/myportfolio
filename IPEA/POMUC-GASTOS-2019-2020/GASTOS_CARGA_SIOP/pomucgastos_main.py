import pyodbc as db
import time

import pomucgastos_processa_carga_siop as pgpc
import pomucgastos_formata_valores as pgfv
import pomucgastos_dados_siop as pgddsiop
import pomucgastos_constantes as pgcst
import pomucgastos_mensagens as pgmsg
import util_database as pgdb
import util_log as pglog
import util_config_formatos as pgcf


def principal():
    """ Texto.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs:
    """
    # abre uma conexao com o banco de dados
    conn = pgdb.get_connection_database(
        pgcst.NM_DRIVER,
        pgcst.NM_SERVER,
        pgcst.NM_DATABASE)
    
    # monta a estrutura de diretorios e arquivos do siop
    dict_siop_completo = pgddsiop.monta_arvore_diretorios_arquivos_importacao(
        pgcst.LT_ANOS_ANALISADOS_SIOP,
        pgcst.NM_PREFIXO_DIRETORIO_DADOS,
        pgcst.NM_DIRETORIO_RAIZ_DADOS,
        verbose = True)
    
    # prepara lista de arquivos para importacao
    lt_arquivos_siop_completo = pgddsiop.get_lista_arquivos_siop_by_dict(
        pgcst.LT_ANOS_ANALISADOS_SIOP,
        dict_siop_completo)
    
    # executa o processamento da carga
    pgpc.processa_carga(conn = conn, lt_arquivos_import = lt_arquivos_siop_completo)

# executa metodo Main da aplicacao
principal()