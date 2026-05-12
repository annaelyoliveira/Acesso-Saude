import pandas as pd
from sqlalchemy import create_engine

# =========================================================
# CONFIG
# =========================================================

ARQ_MUNICIPIOS = r"dados/tbMunicipio202603.csv"
ARQ_PROFISSIONAIS = r"dados/tbDadosProfissionalSus202603.csv"
ARQ_VINCULOS = r"dados/tbCargaHorariaSus202603.csv"
ARQ_CNES = r"dados/cnes_estabelecimentos.csv"

CHUNKSIZE = 500000

# CONFIG POSTGRES
USUARIO = "postgres"
SENHA = "password"
HOST = "localhost"
PORTA = "5432"
BANCO = "cnes_pb"

# =========================================================
# FUNÇÕES
# =========================================================

def extrair_cnes(x):
    if pd.isna(x):
        return None
    numeros = ''.join(filter(str.isdigit, str(x)))
    return numeros[-7:]


# =========================================================
# MUNICÍPIOS
# =========================================================

print("\nLENDO MUNICÍPIOS...")

municipios = pd.read_csv(ARQ_MUNICIPIOS, sep=";", encoding="latin1", dtype=str)
municipios.columns = municipios.columns.str.strip()

municipios_pb = municipios[
    municipios["CO_SIGLA_ESTADO"] == "PB"
][["CO_MUNICIPIO", "NO_MUNICIPIO"]].copy()

print("Municípios PB:", len(municipios_pb))


# =========================================================
# CNES
# =========================================================

print("\nLENDO CNES...")

cnes = pd.read_csv(ARQ_CNES, sep=";", encoding="latin1", dtype=str)
cnes.columns = cnes.columns.str.strip()

tb_unidades = cnes[cnes["CO_UF"] == "25"][[
    "CO_CNES",
    "NO_FANTASIA",
    "CO_IBGE"
]].copy()

tb_unidades["CO_CNES"] = tb_unidades["CO_CNES"].str.strip().str.zfill(7)
tb_unidades["NO_FANTASIA"] = tb_unidades["NO_FANTASIA"].str.upper().str.strip()

tb_unidades = tb_unidades.drop_duplicates()

print("Unidades PB:", len(tb_unidades))


# =========================================================
# VÍNCULOS
# =========================================================

print("\nLENDO VÍNCULOS...")

vinculos_raw = pd.read_csv(ARQ_VINCULOS, sep=";", encoding="latin1", dtype=str)
vinculos_raw.columns = vinculos_raw.columns.str.strip()

print("\nEXEMPLO DADO NÃO CONFORME:")
print(vinculos_raw["CO_UNIDADE"].head(3).tolist())

vinculos = vinculos_raw[[
    "CO_PROFISSIONAL_SUS",
    "CO_UNIDADE"
]].copy()

vinculos["CO_CNES"] = vinculos["CO_UNIDADE"].apply(extrair_cnes)

print("\nAPÓS TRATAMENTO:")
print(vinculos["CO_CNES"].head(3).tolist())

ids_unidades_pb = set(tb_unidades["CO_CNES"])

vinculos = vinculos[
    vinculos["CO_CNES"].isin(ids_unidades_pb)
].drop_duplicates()

print("Vínculos PB:", len(vinculos))


# =========================================================
# PROFISSIONAIS
# =========================================================

profissionais_ids = set(vinculos["CO_PROFISSIONAL_SUS"])

print("Profissionais necessários:", len(profissionais_ids))

print("\nLENDO PROFISSIONAIS...")

lista = []

for chunk in pd.read_csv(
    ARQ_PROFISSIONAIS,
    sep=";",
    encoding="latin1",
    dtype=str,
    chunksize=CHUNKSIZE
):

    chunk.columns = chunk.columns.str.strip()

    if "CO_PROFISSIONAL_SUS" not in chunk.columns:
        continue

    chunk = chunk[
        chunk["CO_PROFISSIONAL_SUS"].isin(profissionais_ids)
    ][["CO_PROFISSIONAL_SUS", "NO_PROFISSIONAL"]].copy()

    chunk["NO_PROFISSIONAL"] = chunk["NO_PROFISSIONAL"].str.upper().str.strip()

    lista.append(chunk)

    print("Chunk:", len(chunk))

tb_profissionais = pd.concat(lista).drop_duplicates()

print("Profissionais encontrados:", len(tb_profissionais))


# =========================================================
# RELACIONAMENTO
# =========================================================

print("\nCRIANDO RELACIONAMENTO...")

tb_profissional_unidade = vinculos[[
    "CO_PROFISSIONAL_SUS",
    "CO_CNES"
]].drop_duplicates()

print("Relacionamentos:", len(tb_profissional_unidade))


# =========================================================
# ENVIAR PARA POSTGRESQL
# =========================================================

print("\nENVIANDO PARA POSTGRESQL...")

engine = create_engine(
    f"postgresql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"
)

tb_unidades.to_sql(
    "tb_unidades",
    engine,
    if_exists="replace",
    index=False
)

tb_profissionais.to_sql(
    "tb_profissionais",
    engine,
    if_exists="replace",
    index=False,
    chunksize=50000,
    method="multi"
)

tb_profissional_unidade.to_sql(
    "tb_profissional_unidade",
    engine,
    if_exists="replace",
    index=False,
    chunksize=50000,
    method="multi"
)

print("\nBANCO POPULADO COM SUCESSO!")
print("Tabelas criadas:")
print("- tb_unidades")
print("- tb_profissionais")
print("- tb_profissional_unidade")

print("\nPROCESSO FINALIZADO!")