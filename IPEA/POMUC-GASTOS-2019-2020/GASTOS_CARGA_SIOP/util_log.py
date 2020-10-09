import csv
import os
import time
from datetime import date

import util_config_formatos as pgcf


def escreve_log(path_diretorio_log: str, nm_arquivo_log: str, lt_str_info: list):
    """ Texto.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs:
    """
    if os.path.exists(path_diretorio_log):
        nm_novo_arquivo_log = path_diretorio_log + nm_arquivo_log + "-{}-{}.txt".format(date.today(), time.strftime("%H.%M.%S"))
        try:
            with open(nm_novo_arquivo_log, 'w+', encoding = pgcf.ENCODING) as f:
                for item in lt_str_info:
                    f.write("%s\n" % item)
        
            print("[INFO]: o arquivo de log foi criado com sucesso.")
        except OSError as ose:
            print("[EXCEPT]: log_util.escreve_log() -> {}".format(ose))
        finally:
            f.close()
    else:
        print("[ERRO]: o arquivo de log não foi encontrado ou não pôde ser criado.")

