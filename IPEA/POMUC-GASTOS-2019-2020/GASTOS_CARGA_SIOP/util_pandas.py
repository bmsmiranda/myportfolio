import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile


def descobre_max_valor_coluna(lt_campos_df: list, pandas_df: pd.DataFrame):  
    """ Texto.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs:
    """  
    dict_col_max_valor = {}
    for campo in lt_campos_df:
        nm_campo = ''
        vl_tmp = 0
        vl_max  = 0
        
        array_vls_coluna = pandas_df[campo]
        for vl in array_vls_coluna:
            vl_tmp = len(vl)
            if vl_tmp > vl_max:
                nm_campo = campo
                vl_max = vl_tmp
        
        dict_col_max_valor[nm_campo] = vl_max

    return dict_col_max_valor

