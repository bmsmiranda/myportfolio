import pyodbc as db
import time

import pomucgastos_formata_valores as pgfv
import pomucgastos_dados_siop as pgddsiop
import pomucgastos_constantes as pgcst
import pomucgastos_mensagens as pgmsg
import util_database as pgdb
import util_log as pglog
import util_config_formatos as pgcf

def processa_carga(conn: db.Connection, lt_arquivos_import: list, verbose: bool = False):
    """ Texto.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs:
    """
    dict_return_insert: dict = {}
    lt_dict_sumario = []
    lt_msgs_log = []

    print(pgmsg.MSG_INICIO_PROC_CARGA_SIOP.format(time.strftime(pgcf.H_M_S_FORMATADA)))
    lt_msgs_log.append(pgmsg.MSG_INICIO_PROC_CARGA_SIOP.format(time.strftime(pgcf.H_M_S_FORMATADA)))
    
    for i, arquivo_siop in enumerate(lt_arquivos_import):
        qtd_registros_sucesso = 0
        qtd_registros_erro = 0
        
        # le arquivo de dados e inicia o processo da carga
        lt_registros = pgddsiop.get_lista_registros_by_arquivo_dados_siop(
            arquivo_siop,
            pgcst.NM_ABA_ARQUIVO_DADOS)

        len_lt_registros = len(lt_registros)
        str_msg = "[Arquivo]: {} com {} registros.".format(arquivo_siop, len_lt_registros)

        lt_msgs_log.append(str_msg)
        dict_resultado_carga: dict = {}

        # insere no banco cada linha do arquivo de dados carregado
        
        for j, valores in enumerate(lt_registros):
            dict_return_insert = pgdb.insert_registros_database(conn,
                                                                pgcst.NM_DATABASE,
                                                                pgcst.NM_TB_ACAOSIOP,
                                                                pgcst.ARRAY_CAMPOS_SIOP,
                                                                valores)
            
            # incrementa relacao de acertos na carga para cada arquivo
            if pgcst.SUCESSO_KEY in dict_return_insert:                
                qtd_registros_sucesso += 1
            
            # incrementa relacao de erros na carga para cada arquivo
            if pgcst.ERRO_KEY in dict_return_insert:
                lt_msg_erro = dict_return_insert[pgcst.ERRO_KEY]
                for erro_msg in lt_msg_erro:
                    lt_msgs_log.append(erro_msg)                
                qtd_registros_erro += 1
            
            # imprime na console e no arquivo de log a cada lote de registros processados
            if j % pgcst.QTD_LOTE_REGISTROS_PROCESSADOS_LOG == 0:
                str_msg = "[Inserido]: {} de {} registros.".format(j, len_lt_registros)
                lt_msgs_log.append(str_msg)
                print(str_msg)

        str_msg = "[ERRO]: qtd registros em erro: {}".format(qtd_registros_erro)
        lt_msgs_log.append(str_msg)
        print(str_msg)

        # preenche dict para sumario total da carga
        dict_resultado_carga['Arquivo processado'] = pgfv.formata_nm_arquivo_importacao(arquivo_siop)
        dict_resultado_carga['A processar'] = str(len_lt_registros)
        dict_resultado_carga['Corretos'] = str(qtd_registros_sucesso)
        dict_resultado_carga['Erros'] = str(qtd_registros_erro)
        dict_resultado_carga['Expurgo'] = "{}%".format(qtd_registros_erro / len_lt_registros)

        lt_dict_sumario.append(dict_resultado_carga)
        lt_msgs_log.append(dict_resultado_carga)
        

    # loga sumario completo da carga
    lt_msgs_log.append(lt_dict_sumario)
    
    print(pgmsg.MSG_FIM_PROC_CARGA_SIOP.format(time.strftime(pgcf.H_M_S_FORMATADA)))
    lt_msgs_log.append(pgmsg.MSG_FIM_PROC_CARGA_SIOP.format(time.strftime(pgcf.H_M_S_FORMATADA)))

    # escreve em arquivo de logs da importacao
    pglog.escreve_log(pgcst.PATH_ARQUIVO_LOG, pgcst.NM_ARQUIVO_LOG, lt_msgs_log)

