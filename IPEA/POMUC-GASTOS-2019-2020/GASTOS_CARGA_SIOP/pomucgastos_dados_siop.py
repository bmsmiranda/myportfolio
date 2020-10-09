import os
import time
import pandas as pd

import pomucgastos_constantes as pgcst
import pomucgastos_formata_valores as pgfv


def monta_arvore_diretorios_arquivos_importacao(lt_anos_analisados_siop: list,
                                                nm_prefixo_diretorio_dados: str,
                                                nm_diretorio_raiz_dados: str,
                                                verbose: bool = False) -> dict:
    """ Percorre estrutura de diretorios onde estaos os aquivos de dados do SIOP 
    e monta dict com a arvore completa.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs: (a) implementar controle de excecao para caso o parametro seja nulo ou vazio.
           (b) implementar a clausula return com a estrutura montada.
    """
    dict_estrutura_arquivos_siop = {}
    len_total_arquivos = 0

    for ano_siop in lt_anos_analisados_siop:
        diretorio_analisado = nm_prefixo_diretorio_dados + ano_siop
        path_diretorio = os.path.join(nm_diretorio_raiz_dados, diretorio_analisado)
        lt_arquivos_por_ano = []

        # verifica se o path definido estah correto
        if os.path.exists(path_diretorio):
            if verbose:
                print("[INFO]: path do diretorio analisado {}".format(diretorio_analisado))

            # verifica se o path eh um diretorio
            if os.path.isdir(path_diretorio):
                if verbose:
                    print("[INFO]: diretorio de dados {}".format(path_diretorio))
                
                # para cada diretorio, lista o conteudo se estes forem arquivos    
                for item in os.listdir(path_diretorio):                
                    nm_arquivo_completo = os.path.join(path_diretorio, item)

                    if os.path.isfile(nm_arquivo_completo):
                        len_total_arquivos += os.path.getsize(nm_arquivo_completo)
                        lt_arquivos_por_ano.append(nm_arquivo_completo)

                        if verbose:
                            print("[INFO]: arquivo de dados encontrado {}".format(nm_arquivo_completo))
                
                # popula dict com a estrutura dos anos e lista de arquivos referentes para o SIOP 
                dict_estrutura_arquivos_siop[ano_siop] = lt_arquivos_por_ano
    
    print("[INFO]: tamanho da estrutura de diretorios/arquivos: {}".format(len(dict_estrutura_arquivos_siop)))
    print("[INFO]: tamanho total do arquivo de dados agregado {}".format(len_total_arquivos))

    if verbose:
        print("[INFO]: estrutura de diretorios/arquivos")    
        print("|")
        for estrutura in dict_estrutura_arquivos_siop:
            print("|-- {}".format(estrutura))
            lt_arquivos = dict_estrutura_arquivos_siop.get(estrutura)
            
            for arquivo in lt_arquivos:
                print("\t|-- {}".format(arquivo))
    
    return dict_estrutura_arquivos_siop

def get_lista_registros_by_arquivo_dados_siop(nm_arquivo_dados: str, nm_aba_dados: str) -> list:
    """ Lê aquivo de dados em estrutura do SIOP.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs:
    """
    df_excel_data: pd.DataFrame = None
    if nm_arquivo_dados != "" and nm_aba_dados != "":
        print("[INFO]: inicio da leitura em {}.".format(time.strftime("%H:%M:%S")))
        
        df_excel_data = pd.read_excel(nm_arquivo_dados, sheet_name = nm_aba_dados)

        print("[INFO]: leitura finalizada em {}.".format(time.strftime("%H:%M:%S")))

        if df_excel_data is not None and df_excel_data.size > 0:
            print("[INFO]: o DataFrame possui {} registros totais.".format(df_excel_data.size))
            print("[INFO]: o DataFrame possui {} colunas.".format(df_excel_data.columns.size))
            print("[INFO]: o DataFrame possui {} linhas.".format(len(df_excel_data.index)))

            lt_registros_siop = []
            print("[INFO]: inicio do processamento em {}.".format(time.strftime("%H:%M:%S")))

            # preenche os valores NaN com o valor zero(0)
            df_excel_data = df_excel_data.fillna(0)
            # remove temporariamente a coluna de dados
            df_excel_data.pop('Programa (desc.)')
        
            for indice, row in df_excel_data.iterrows():
                lt_linha_by_pandas_series = row.tolist()
                lt_linha_by_pandas_series.append(pgfv.formata_nm_arquivo_importacao(nm_arquivo_dados))

                # corresponde a linha na planilha importada
                lt_linha_by_pandas_series.append(indice + pgcst.QTD_LINHAS_PRIMEIRO_REGISTRO)
                lt_registros_siop.append(lt_linha_by_pandas_series)
                       
            print("[INFO]: processado o arquivo {}.".format(nm_arquivo_dados))
            print("[INFO]: fim do processamento em {}.".format(time.strftime("%H:%M:%S")))
            print("[INFO]: lista implementada com {} registros.".format(len(lt_registros_siop)))
    else:
        print("[ERRO]: os parâmetros de leitura estão incorretos.")
    
    return lt_registros_siop

def get_lista_arquivos_siop_by_dict(lt_anos_analisados_siop: list,
                                    dict_estrutura_arquivos_siop: dict) -> list:
    """ Texto. 
    Args:
    Returns:
    Raises:
    IOError:
    TODOs:
    """
    lt_arquivos_import_siop = []

    for ano_siop in lt_anos_analisados_siop:
        lt_by_ano = []
        if ano_siop in dict_estrutura_arquivos_siop:
            lt_by_ano = dict_estrutura_arquivos_siop[ano_siop]

        for registro in lt_by_ano:
            lt_arquivos_import_siop.append(registro)

    return lt_arquivos_import_siop

