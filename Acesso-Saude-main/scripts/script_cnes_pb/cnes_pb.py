
import pandas as pd
import re
from sqlalchemy import create_engine

cnes = pd.read_csv(r"C:\Users\andre\OneDrive\Documentos\IFPB-estudo\BD2\cnes_estabelecimentos_csv/cnes_estabelecimentos.csv", sep = ";", encoding = "ISO-8859-1", low_memory= False)

cnes_pb = cnes[cnes["CO_UF"] == 25][["TP_UNIDADE","CO_UF", "NO_FANTASIA", "NO_LOGRADOURO", "NU_ENDERECO", "NO_BAIRRO", "NU_TELEFONE", "CO_TURNO_ATENDIMENTO", "DS_TURNO_ATENDIMENTO","NO_EMAIL","CO_IBGE",
  "ST_CENTRO_CIRURGICO",
 "ST_CENTRO_OBSTETRICO",
 "ST_CENTRO_NEONATAL",
 "ST_ATEND_HOSPITALAR",
 "ST_SERVICO_APOIO",
 "ST_ATEND_AMBULATORIAL",]].copy()


def limpar(texto):
  if isinstance(texto, str):
    return texto.strip()
  return texto

cnes_pb["NU_TELEFONE"] = cnes_pb["NU_TELEFONE"].astype(str)
cnes_pb['NO_EMAIL'] = cnes_pb['NO_EMAIL'].astype(str)
cnes_pb = cnes_pb.map(limpar)

cnes_pb = cnes_pb.replace(['', 'NAN', 'NaN', 'nan', 'null', 'NULL', 'S/N', 'nan.0'], None)

cnes_pb['CO_TURNO_ATENDIMENTO'] = (cnes_pb['CO_TURNO_ATENDIMENTO'].fillna(0).astype(int))
cnes_pb['ST_CENTRO_CIRURGICO'] = (cnes_pb['ST_CENTRO_CIRURGICO'].fillna(0).astype(int))
cnes_pb['ST_CENTRO_OBSTETRICO'] = (cnes_pb['ST_CENTRO_OBSTETRICO'].fillna(0).astype(int))
cnes_pb['ST_CENTRO_NEONATAL'] = (cnes_pb['ST_CENTRO_NEONATAL'].fillna(0).astype(int))
cnes_pb['ST_ATEND_HOSPITALAR'] = (cnes_pb['ST_ATEND_HOSPITALAR'].fillna(0).astype(int))
cnes_pb['ST_SERVICO_APOIO'] = (cnes_pb['ST_SERVICO_APOIO'].fillna(0).astype(int))
cnes_pb['ST_ATEND_AMBULATORIAL'] = (cnes_pb['ST_ATEND_AMBULATORIAL'].fillna(0).astype(int))


def padronizar_telefone(telefone):
  if telefone is None or pd.isna(telefone):
    return None

  telefone = re.sub(r'[^0-9]', '', str(telefone))
  if len(telefone) < 8:
    return None
  if len(telefone) in [8, 9]:
    return "(83)" + telefone
  if len(telefone) == 10:
    return  f'({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}'
  elif len(telefone) == 11:
    return f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}'
  else:
    return None

cnes_pb['NU_TELEFONE'] = cnes_pb['NU_TELEFONE'].apply(padronizar_telefone)


correcoes_logradouro = {
r'\bAV\b|\bAVN\b|\bAVA\b|\bAVENDIDA\b|\bAVENIADA\b': 'AVENIDA',
r'\bR\b|\bRU\b|\bR/\b': 'RUA',
r'\bTV\b|\bTRAV\b': 'TRAVESSA',
r'\bPCA\b|\bPRC\b|\bPC\b|\bPRAC\b': 'PRAÇA',
r'\bDR\b|\bDOUTOU\b': 'DOUTOR',
r'\bDRA\b': 'DOUTORA',
r'\bVERIADOR\b': 'VEREADOR',
r'\bDSITRITO\b|\bDESTRITO\b': 'DISTRITO',
r'\bCONJJUNTO\b': 'CONJUNTO',
r'\bSIT\b': 'SITIO',
r'\bPROF\b': 'PROFESSOR',
r'\bGOV\b': 'GOVERNADOR'
}

cnes_pb['NO_LOGRADOURO'] = cnes_pb['NO_LOGRADOURO'].str.upper()
cnes_pb['NO_LOGRADOURO'] = cnes_pb['NO_LOGRADOURO'].replace(correcoes_logradouro, regex=True)
cnes_pb['NO_LOGRADOURO'] = cnes_pb['NO_LOGRADOURO'].apply(limpar)
cnes_pb['NO_FANTASIA'] = cnes_pb['NO_FANTASIA'].str.upper()
cnes_pb['NO_BAIRRO'] = cnes_pb['NO_BAIRRO'].str.upper()
cnes_pb['NO_EMAIL'] = cnes_pb['NO_EMAIL'].str.lower()


tipos_unidade_data = {
    "01": "POSTO DE SAÚDE",
    "02": "CENTRO DE SAUDE/UNIDADE BASICA",
    "04": "POLICLINICA",
    "05": "HOSPITAL GERAL",
    "07": "HOSPITAL ESPECIALIZADO",
    "15": "UNIDADE MISTA",
    "20": "PRONTO ATENDIMENTO",
    "21": "PRONTO SOCORRO GERAL",
    "36": "CLINICA/CENTRO DE ESPECIALIDADE",
    "43": "FARMACIA",
    "60": "COOPERATIVA",
    "67": "LABORATORIO CENTRAL DE SAUDE PUBLICA"
}

cnes_pb['CO_IBGE'] = cnes_pb['CO_IBGE'].astype(str)
cnes_tipos_unidade = pd.DataFrame(list(tipos_unidade_data.items()), columns=['TP_UNIDADE', 'DS_TP_UNIDADE'])
cnes_tipos_unidade['TP_UNIDADE'] = cnes_tipos_unidade['TP_UNIDADE'].astype(int)

cidades_pb = {
    "250010": "ÁGUA BRANCA", "250020": "AGUIAR", "250030": "ALAGOA GRANDE", "250040": "ALAGOA NOVA",
    "250050": "ALAGOINHA", "250053": "ALCANTIL", "250057": "ALGODÃO DE JANDAÍRA", "250060": "ALHANDRA",
    "250070": "SÃO JOÃO DO RIO DO PEIXE", "250073": "AMPARO", "250077": "APARECIDA", "250080": "ARAÇAGI",
    "250090": "ARARA", "251000": "ARARUNA", "250110": "AREIA", "250115": "AREIA DE BARAÚNAS",
    "250120": "AREIAL", "250130": "AROEIRAS", "250135": "ASSUNÇÃO", "250140": "BAÍA DA TRAIÇÃO",
    "250150": "BANANEIRAS", "250153": "BARAÚNA", "250157": "BARRA DE SANTANA", "250160": "BARRA DE SANTA ROSA",
    "250170": "BARRA DE SÃO MIGUEL", "250180": "BAYEUX", "250190": "BELÉM", "250200": "BELÉM DO BREJO DO CRUZ",
    "250205": "BERNARDINO BATISTA", "250210": "BOA VENTURA", "250215": "BOA VISTA", "250220": "BOM JESUS",
    "250230": "BOM SUCESSO", "250240": "BONITO DE SANTA FÉ", "250250": "BOQUEIRÃO", "250260": "IGARACY",
    "250270": "BORBOREMA", "250280": "BREJO DO CRUZ", "250290": "BREJO DOS SANTOS", "250300": "CAAPORÃ",
    "250310": "CABACEIRAS", "250320": "CABEDELO", "250330": "CACHOEIRA DOS ÍNDIOS", "250340": "CACIMBA DE AREIA",
    "250350": "CACIMBA DE DENTRO", "250355": "CACIMBAS", "250360": "CAIÇARA", "250370": "CAJAZEIRAS",
    "250375": "CAJAZEIRINHAS", "250380": "CALDAS BRANDÃO", "250390": "CAMALAÚ", "250400": "CAMPINA GRANDE",
    "250403": "CAPIM", "250407": "CARAÚBAS", "250410": "CARRAPATEIRA", "250415": "CASSERENGUE",
    "250420": "CATINGUEIRA", "250430": "CATOLÉ DO ROCHA", "250435": "CATURITÉ", "250440": "CONCEIÇÃO",
    "250450": "CONDADO", "250460": "CONDE", "250470": "CONGO", "250480": "COREMAS",
    "250485": "COXIXOLA", "250490": "CRUZ DO ESPÍRITO SANTO", "250500": "CUBATI", "250510": "CUITÉ",
    "250520": "CUITEGI", "250523": "CUITÉ DE MAMANGUAPE", "250527": "CURRAL DE CIMA", "250530": "CURRAL VELHO",
    "250535": "DAMIÃO", "250540": "DESTERRO", "250550": "VISTA SERRANA", "250560": "DIAMANTE",
    "250570": "DONA INÊS", "250580": "DUAS ESTRADAS", "250590": "EMAS", "250600": "ESPERANÇA",
    "250610": "FAGUNDES", "250620": "FREI MARTINHO", "250625": "GADO BRAVO", "250630": "GUARABIRA",
    "250640": "GURINHÉM", "250650": "GURJÃO", "250660": "IBIARA", "250670": "IMACULADA",
    "250680": "INGÁ", "250690": "ITABAIANA", "250700": "ITAPORANGA", "250710": "ITAPOROROCA",
    "250720": "ITATUBA", "250730": "JACARAÚ", "250740": "JERICÓ", "250750": "JOÃO PESSOA",
    "250760": "JUAREZ TÁVORA", "250770": "JUAZEIRINHO", "250780": "JUNCO DO SERIDÓ", "250790": "JURIPIRANGA",
    "250800": "JURU", "250810": "LAGOA", "250820": "LAGOA DE DENTRO", "250830": "LAGOA SECA",
    "250840": "LASTRO", "250850": "LIVRAMENTO", "250855": "LOGRADOURO", "250860": "LUCENA",
    "250870": "MÃE D'ÁGUA", "250880": "MALTA", "250890": "MAMANGUAPE", "250900": "MANAÍRA",
    "250905": "MARCAÇÃO", "250910": "MARI", "250915": "MARIZÓPOLIS", "250920": "MASSARANDUBA",
    "250930": "MATARACA", "250933": "MATINHAS", "250937": "MATO GROSSO", "250939": "MATURÉIA",
    "250940": "MOGEIRO", "250950": "MONTADAS", "250960": "MONTE HOREBE", "250970": "MONTEIRO",
    "250980": "MULUNGU", "250990": "NATUBA", "251000": "NAZAREZINHO", "251010": "NOVA FLORESTA",
    "251020": "NOVA OLINDA", "251030": "NOVA PALMEIRA", "251040": "OLHO D'ÁGUA", "251050": "OLIVEDOS",
    "251060": "OURO VELHO", "251065": "PARARI", "251070": "PASSAGEM", "251080": "PATOS",
    "251090": "PAULISTA", "251100": "PEDRA BRANCA", "251110": "PEDRA LAVRADA", "251120": "PEDRAS DE FOGO",
    "251130": "PIANCÓ", "251140": "PICUÍ", "251150": "PILAR", "251160": "PILÕES",
    "251170": "PILÕEZINHOS", "251180": "PIRPIRITUBA", "251190": "PITIMBU", "251200": "POCINHOS",
    "251203": "POÇO DANTAS", "251207": "POÇO DE JOSÉ DE MOURA", "251210": "POMBAL", "251220": "PRATA",
    "251230": "PRINCESA ISABEL", "251240": "PUXINANÃ", "251250": "QUEIMADAS", "251260": "QUIXABA",
    "251270": "REMÍGIO", "251272": "PEDRO RÉGIS", "251274": "RIACHÃO", "251275": "RIACHÃO DO BACAMARTE",
    "251276": "RIACHÃO DO POÇO", "251278": "RIACHO DE SANTO ANTÔNIO", "251280": "RIACHO DOS CAVALOS", "251290": "RIO TINTO",
    "251300": "SALGADINHO", "251310": "SALGADO DE SÃO FÉLIX", "251315": "SANTA CECÍLIA", "251320": "SANTA CRUZ",
    "251330": "SANTA HELENA", "251335": "SANTA INÊS", "251340": "SANTA LUZIA", "251350": "SANTANA DE MANGUEIRA",
    "251360": "SANTANA DOS GARROTES", "251365": "JOCA CLAUDINO", "251370": "SANTA RITA", "251380": "SANTA TERESINHA",
    "251385": "SANTO ANDRÉ", "251390": "SÃO BENTO", "251392": "SÃO BENTINHO", "251394": "SÃO DOMINGOS DO CARIRI",
    "251396": "SÃO DOMINGOS", "251398": "SÃO FRANCISCO", "251400": "SÃO JOÃO DO CARIRI", "251410": "SÃO JOÃO DO TIGRE",
    "251420": "SÃO JOSÉ DA LAGOA TAPADA", "251430": "SÃO JOSÉ DE CAIANA", "251440": "SÃO JOSÉ DE ESPINHARAS", "251445": "SÃO JOSÉ DOS RAMOS",
    "251450": "SÃO JOSÉ DE PIRANHAS", "251455": "SÃO JOSÉ DE PRINCESA", "251460": "SÃO JOSÉ DO BONFIM", "251465": "SÃO JOSÉ DO BREJO DO CRUZ",
    "251470": "SÃO JOSÉ DO SABUGI", "251480": "SÃO JOSÉ DOS CORDEIROS", "251490": "SÃO MAMEDE", "251500": "SÃO MIGUEL DE TAIPU",
    "251510": "SÃO SEBASTIÃO DE LAGOA DE ROÇA", "251520": "SÃO SEBASTIÃO DO UMBUZEIRO", "251530": "SAPÉ", "251540": "SÃO VICENTE DO SERIDÓ",
    "251550": "SERRA BRANCA", "251560": "SERRA DA RAIZ", "251570": "SERRA GRANDE", "251580": "SERRA REDONDA",
    "251590": "SERRARIA", "251593": "SERTÃOZINHO", "251597": "SOBRADO", "251600": "SOLÂNEA",
    "251610": "SOLEDADE", "251615": "SOSSÊGO", "251620": "SOUSA", "251630": "SUMÉ",
    "251640": "TACIMA", "251650": "TAPEROÁ", "251660": "TAVARES", "251670": "TEIXEIRA",
    "251675": "TENÓRIO", "251680": "TRIUNFO", "251690": "UIRAÚNA", "251700": "UMBUZEIRO",
    "251710": "VÁRZEA", "251720": "VIEIRÓPOLIS", "251740": "ZABELÊ"
}
cnes_cidades = pd.DataFrame(list(cidades_pb.items()), columns=['CO_IBGE', 'NO_MUNICIPIO'])
cnes_pb["ID_ENDERECO"] = range(1, len(cnes_pb) + 1)
cnes_enderecos = cnes_pb[["NO_LOGRADOURO", "NU_ENDERECO", "NO_BAIRRO", "CO_IBGE", "ID_ENDERECO", "CO_UF"]].copy()

cnes_pb['ST_CENTRO_CIRURGICO'] = cnes_pb['ST_CENTRO_CIRURGICO'].fillna(0)
cnes_pb['ST_CENTRO_CIRURGICO'] = cnes_pb['ST_CENTRO_CIRURGICO'].astype(int) 
cnes_pb['ST_CENTRO_CIRURGICO'] = cnes_pb['ST_CENTRO_CIRURGICO'].astype(bool)

cnes_pb['ST_CENTRO_OBSTETRICO'] = cnes_pb['ST_CENTRO_OBSTETRICO'].fillna(0)
cnes_pb['ST_CENTRO_OBSTETRICO'] = cnes_pb['ST_CENTRO_OBSTETRICO'].astype(int)
cnes_pb['ST_CENTRO_OBSTETRICO'] = cnes_pb['ST_CENTRO_OBSTETRICO'].astype(bool)

cnes_pb['ST_CENTRO_NEONATAL'] = cnes_pb['ST_CENTRO_NEONATAL'].fillna(0)
cnes_pb['ST_CENTRO_NEONATAL'] = cnes_pb['ST_CENTRO_NEONATAL'].astype(int)
cnes_pb['ST_CENTRO_NEONATAL'] = cnes_pb['ST_CENTRO_NEONATAL'].astype(bool)

cnes_pb['ST_ATEND_HOSPITALAR'] = cnes_pb['ST_ATEND_HOSPITALAR'].fillna(0)
cnes_pb['ST_ATEND_HOSPITALAR'] = cnes_pb['ST_ATEND_HOSPITALAR'].astype(int)
cnes_pb['ST_ATEND_HOSPITALAR'] = cnes_pb['ST_ATEND_HOSPITALAR'].astype(bool)

cnes_pb['ST_SERVICO_APOIO'] = cnes_pb['ST_SERVICO_APOIO'].fillna(0)
cnes_pb['ST_SERVICO_APOIO'] = cnes_pb['ST_SERVICO_APOIO'].astype(int)
cnes_pb['ST_SERVICO_APOIO'] = cnes_pb['ST_SERVICO_APOIO'].astype(bool)

cnes_pb['ST_ATEND_AMBULATORIAL'] = cnes_pb['ST_ATEND_AMBULATORIAL'].fillna(0)
cnes_pb['ST_ATEND_AMBULATORIAL'] = cnes_pb['ST_ATEND_AMBULATORIAL'].astype(int)
cnes_pb['ST_ATEND_AMBULATORIAL'] = cnes_pb['ST_ATEND_AMBULATORIAL'].astype(bool)

cnes_turnos = cnes_pb[["CO_TURNO_ATENDIMENTO", "DS_TURNO_ATENDIMENTO"]].drop_duplicates().dropna().copy()
cnes_capacidades = cnes_pb[[ 'ID_ENDERECO', 'ST_CENTRO_CIRURGICO', 'ST_CENTRO_OBSTETRICO', 'ST_CENTRO_NEONATAL', 'ST_ATEND_HOSPITALAR', 'ST_SERVICO_APOIO', 'ST_ATEND_AMBULATORIAL']].copy()
cnes_unidades = cnes_pb[["NO_FANTASIA", "TP_UNIDADE", "NU_TELEFONE", "NO_EMAIL", "CO_TURNO_ATENDIMENTO", "ID_ENDERECO"]].copy()

USUARIO = "postgres"
SENHA = "password"
HOST = "localhost"
PORTA = "5432"
BANCO = "cnes_pb"

engine = create_engine(f"postgresql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}")

cnes_cidades.to_sql(name = "tb_cidades", con = engine, if_exists = "replace", index = False)
cnes_turnos.to_sql(name = "tb_turnos", con = engine, if_exists = "replace", index = False)
cnes_enderecos.to_sql(name = "tb_enderecos", con = engine, if_exists = "replace", index = False)
cnes_tipos_unidade.to_sql(name="tb_tipos_unidade", con=engine, if_exists="replace", index=False)
cnes_capacidades.to_sql(name="tb_capacidades", con=engine, if_exists="replace", index=False)
cnes_unidades.to_sql(name = "tb_unidades", con = engine, if_exists = "replace", index = False)
