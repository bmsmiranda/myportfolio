import pomucgastos_constantes as pgcst
import pyodbc as db


def get_connection_database(nm_driver: str, nm_server: str, nm_database: str) -> db.Connection:
    """ Abre conexão com o banco de dados especificado.
    Args:
    Returns:
    Raises:
    IOError:    
    TODOs: implementar o controle de excecoes e singleton
    """
    try:
        conn = db.connect('Driver=' + nm_driver + ';'
                          'Server=' + nm_server + ';'
                          'Database=' + nm_database + ';'
                          'Trusted_Connection=yes;')
        print("[INFO]: conexão efetuada com sucesso.")
        
    except db.DatabaseError as de:
        print("[ERRO]: falha ao obter a conexão.")
        print("[EXCEPT]: database_util.get_connection_database() -> {}".format(de))

    return conn

def select_lista_registros_database(conn: db.Connection,
                                    nm_tabela: str, 
                                    lt_campos_select: list,
                                    condicao_where: str = None,
                                    condicao_groupby: str = None,
                                    condicao_orderby: str = None,
                                    str_select_completo_formatado: str = None) -> list:
    """ Manipula registros de SELECT no banco de dados especificado.
    Args:
    Returns:
    Raises:
    IOError:    
    TODOs: implementar o controle de excecoes.
    """
    str_linha_resultado_select = ''
    lt_registros_selecionados = []    
    
    if conn != None:
        print("[INFO]: conexão efetuada com sucesso.")
    else:
        print("[ERRO]: falha ao obter a conexão.")

    try:
        cursor = conn.cursor()
        
        if str_select_completo_formatado != None and str_select_completo_formatado != "":
            cursor.execute(str_select_completo_formatado)
        else:
            pass

        linha = cursor.fetchone()
    except db.DatabaseError as de:
        print("[EXCEPT]: database_util.get_lista_registros_database() -> {}".format(de))

    while linha:
        str_linha_resultado_select = str(linha)
        lt_registros_selecionados.append(str_linha_resultado_select)
        linha = cursor.fetchone()

    return lt_registros_selecionados

def insert_registros_database(conn: db.Connection, 
                              nm_database: str, 
                              nm_tabela: str, 
                              lt_campos_insert: list,
                              lt_valores_insert: list,
                              verbose: bool = False,
                              log: bool = False,
                              lt_registros_log: list = None):
    """ Manipula registros de INSERT no banco de dados especificado.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs: (a) implementar o controle de excecoes.
           (b) implementar o insert de maneira generica
    """   
    if conn != None:
        if verbose == True:
            print("[INFO]: a conexão foi encontrada.")
    else:
        if verbose == True:
            print("[ERRO]: a conexão não foi encontrada.")
        return
    
    # formata a saida do metodo em erros e sucesso
    lt_msg_erros = []
    dict_return_metodo: dict = {}
    
    str_clausula_insert = "INSERT INTO " + nm_database + ".dbo." + nm_tabela
    str_clausula_insert += monta_clausula_insert_by_array(lt_campos_insert)              
    str_clausula_values = 'VALUES ('

    len_lt_valores_insert = len(lt_valores_insert)
    for idx, valor in enumerate(lt_valores_insert):
        if isinstance(valor, (str)):
            # tratamento de caracteres especiais
            valor = valor.replace('\\', '')
            valor = valor.replace('\'', '')
            
            str_clausula_values += "{}{}{}".format('\'', valor, '\'')

        elif isinstance(valor, (int)):
            str_clausula_values += "{}".format(valor)
        elif isinstance(valor, (float)):
            str_clausula_values += "{}".format(valor)
        
        if idx < (len_lt_valores_insert - 1):
            str_clausula_values += ","
    
    # formata a string de valores do insert
    str_clausula_values += ')'
    str_clausula_values = str_clausula_values.replace('[', '')
    str_clausula_values = str_clausula_values.replace(']', '')
    str_insert_formatado = str_clausula_insert + str_clausula_values

    try:
        cursor = conn.cursor()
        cursor.execute(str_insert_formatado)
        conn.commit()
        dict_return_metodo[pgcst.SUCESSO_KEY] = "o registro foi inserido com sucesso."
        
        if verbose == True:
            print("[INFO]: o registro foi inserido com sucesso.")
            print("[INFO]: {}".format(str_insert_formatado))

    except db.DataError as de:
        msg_except = "[ERRO]: \n {}".format(str_insert_formatado)
        lt_msg_erros.append(msg_except)
        print(msg_except)

        msg_except = "[EXCEPT]: database_util.insert_registros_database() -> {}".format(de)
        lt_msg_erros.append(msg_except)
        print(msg_except)
    
    if len(lt_msg_erros) > 0:
        dict_return_metodo[pgcst.ERRO_KEY] = lt_msg_erros
    
    return dict_return_metodo

def monta_clausula_insert_by_array(array_campos: list) -> str:
    """ Texto.
    Args:
    Returns:
    Raises:
    IOError:
    TODOs:
    """
    str_campos_insert = " ("
    len_array_campos = len(array_campos)

    for idx, campo in enumerate(array_campos):
        str_campos_insert += campo
        if idx < (len_array_campos - 1):
            str_campos_insert += ","

    str_campos_insert += ") "

    return str_campos_insert

