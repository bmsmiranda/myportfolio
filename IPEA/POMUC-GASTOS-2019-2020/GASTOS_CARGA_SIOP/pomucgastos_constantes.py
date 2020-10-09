# parametrizacoes da carga
QTD_LOTE_REGISTROS_PROCESSADOS_LOG = 1000
PATH_ARQUIVO_LOG = "L:\\Projeto_POMUC_2019\\Log\\"
NM_ARQUIVO_LOG = "pomucgastoslog"


# utilizado para indicar a configuracao dos dados a serem importados
NM_DIRETORIO_RAIZ_DADOS = "L:\\Projeto_POMUC_2019\\Base_Bruta\\" # [IPEA]
NM_PREFIXO_ARQUIVO = "Extrator"
NM_ABA_ARQUIVO_DADOS = "Dados"
NM_PREFIXO_DIRETORIO_DADOS = "SIOP_"
QTD_LINHAS_PRIMEIRO_REGISTRO = 2


# confiuracoes do banco de dados
NM_SERVER = 'MSSQL2016\\Pesquisa' #'CV-BMNOTE\\CVALUEPROD'
NM_DATABASE = 'POMUC_GASTOS'
NM_DRIVER = '{SQL Server Native Client 11.0}'
USER_NAME = 'Bruno'
PASSWORD = '1'
# nome das tabelas do banco POMUC_GASTOS
#NM_TB_ACAOSIOP = "AcaoSIOP_N"
NM_TB_ACAOSIOP = "AcaoSIOP"

# chaves(key) das estruturas Python:dict
ERRO_KEY = "ERRO"
SUCESSO_KEY = "SUCESSO"


# utilizado para verificar os valores maximos das colunas antes da importacao
ARRAY_CAMPOS_STR_SIOP = ['Esfera (desc.)', 
                         'Órgão (desc.)',
                         'Unidade Orçamentária (desc.)',
                         'Função (desc.)', 
                         'Subfunção (desc.)',
                         'Programa (desc.)', 
                         'Programa (ano, desc.)',
                         'Objetivo (desc.)', 
                         'Iniciativa (desc.)', 
                         'Ação (ano, desc.)',
                         'Tipo de Ação (desc.)', 
                         'Subtipo de Ação (desc.)', 
                         'Localizador (ano, desc.)', 
                         'Plano Orçamentário (ano, desc.)',
                         'Município (desc.)',
                         'UF (desc.)', 
                         'IDOC (desc.)',
                         'IDUSO (desc.)', 
                         'Fonte (desc.)', 
                         'Natureza de Despesa (desc.)', 
                         'GND (desc.)', 
                         'Modalidade (desc.)', 
                         'Elemento de Despesa (desc.)']


# anos que serao analisados do SIOP
"""
LT_ANOS_ANALISADOS_SIOP = ("2000", "2001", "2002", "2003", "2004",
                           "2005", "2006", "2007", "2008", "2009",
                           "2010", "2011", "2012", "2013", "2014",
                           "2015", "2016", "2017", "2018", "2019")
"""
LT_ANOS_ANALISADOS_SIOP = ("2003", "2011", "2016")


#
STR_ESTRUTURA_CLAUSULA_INSERT_SIOP = """
    INSERT INTO POMUC_GASTOS.dbo.AcaoSIOP (        
        AnoExercicio,AnoReferencia,
        IdEsfera,Esfera,IdOrgao,Orgao,
        IdUnidadeOrcamentaria,UnidadeOrcamentaria,
        Poder,IdFuncao,Funcao,
        IdSubFuncao,SubFuncao,
        IdPrograma,Programa, --variavel 'AnoPrograma' retirada
        Objetivo,Iniciativa,
        IdAcao,Acao, --variavel 'AnoAcao' retirada
        AcaoTipo,AcaoSubTipo,
        LocalizadorSIOP,LocalizadorSIOPDescricao,
        PlanoOrcamentario, --variavel 'AnoPlanoOrcamentario' retirada
        Municipio,UF,
        IdOperacaoCredito,OperacaoCredito,
        IdUso,Uso,
        IdFonte,Fonte,
        IdNaturezaDespesa,NaturezaDespesa,
        IdGrandeNaturezaDespesa,GrandeNaturezaDespesa,
        IdModalidade,Modalidade,
        IdElementoDespesa,ElementoDespesa,
        ValorLOA,ValorAutorizado,
        ValorEmpenhado,ValorEmpenhadoLiquidado,
        ValorPago,ValorPagoRAPPago,
        ArquivoImportacao,
        IndiceLinha
    )"""


#
ARRAY_CAMPOS_SIOP = ['AnoExercicio',
                     'AnoReferencia',
                     'IdEsfera,Esfera',
                     'IdOrgao',
                     'Orgao',
                     'IdUnidadeOrcamentaria',
                     'UnidadeOrcamentaria',
                     'Poder',
                     'IdFuncao',
                     'Funcao',
                     'IdSubFuncao',
                     'SubFuncao',
                     'IdPrograma',
                     'Programa',
                     'Objetivo',
                     'Iniciativa',
                     'IdAcao',
                     'Acao',
                     'AcaoTipo',
                     'AcaoSubTipo',
                     'LocalizadorSIOP',
                     'LocalizadorSIOPDescricao',
                     'PlanoOrcamentario',
                     'Municipio',
                     'UF',
                     'IdOperacaoCredito',
                     'OperacaoCredito',
                     'IdUso',
                     'Uso',
                     'IdFonte',
                     'Fonte',
                     'IdNaturezaDespesa',
                     'NaturezaDespesa',
                     'IdGrandeNaturezaDespesa',
                     'GrandeNaturezaDespesa',
                     'IdModalidade',
                     'Modalidade',
                     'IdElementoDespesa',
                     'ElementoDespesa',
                     'ValorLOA',
                     'ValorAutorizado',
                     'ValorEmpenhado',
                     'ValorEmpenhadoLiquidado',
                     'ValorPago',
                     'ValorPagoRAPPago',
                     'ArquivoImportacao',
                     'IndiceLinha']

