import pandas as pd

import util_diretorios as pgdir
import util_pandas as pgpd
import util_log as pglog
import pomucgastos_constantes as pgcst
import pomucgastos_dados_siop as pgddsiop


# teste dos metodos de 'diretorios_util'
"""
pgdir.exibe_conteudo_diretorios(pgcst.NM_DIRETORIO_RAIZ_DADOS)
"""


# teste dos metodos do pacote pomucgastos 'pandas_util'
"""
pandas_df = pd.read_excel('C:\\Data\\POMUC_2019\\Extrator_2018_f1_resumido.xlsx', sheet_name='Dados')
dict_retorno = pgpd.descobre_max_valor_coluna(pg_cst.ARRAY_CAMPOS_STR, pandas_df)
print(type(dict_retorno))
print(dict_retorno)
"""


# teste dos metodos do pacote pomucgastos 'log_util'
"""
dict_resultado_carga: dict = {}
dict_resultado_carga['Arquivo processado'] = "Extrator1576612595340_2017_f4.xlsx"
dict_resultado_carga['A processar'] = "100.000"
dict_resultado_carga['Corretos'] = "100.000"
dict_resultado_carga['Erros'] = "0"
dict_resultado_carga['Expurgo'] = "0%"
"""
"""
lt_msgs_log = ['o', 'log', 'ficou', 'bom', 'e rapido']
"""
"""
lt_msgs_log = [dict_resultado_carga]
pglog.escreve_log('C:\\Projetos\\POMUC_2019\\Log\\', 'teste-pomucgastoslog', lt_msgs_log)
"""


# teste dos metodos do pacote pomucgastos 'pomucgastos_dados_siop'
"""
dict_siop = pgddsiop.monta_arvore_diretorios_arquivos_importacao(pgcst.LT_ANOS_ANALISADOS_SIOP,
                                                                 pgcst.NM_PREFIXO_DIRETORIO_DADOS,
                                                                 pgcst.NM_DIRETORIO_RAIZ_DADOS)
lista = pgddsiop.get_lista_arquivos_siop_by_dict(pgcst.LT_ANOS_ANALISADOS_SIOP,
                                             dict_siop)
for el in lista:
    print(el)
"""

"""
PATH_ARQUIVO_REDE = "C:\\Data\\POMUC_2019\\Extrator_2018_f1_resumido.xlsx"
lista = pgddsiop.get_lista_arquivos_dados_siop(PATH_ARQUIVO_REDE, pg_cst.NM_ABA_ARQUIVO_DADOS)
print(len(lista))
print(lista[:2])
"""

