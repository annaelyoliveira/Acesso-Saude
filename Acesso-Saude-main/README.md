# Acesso Saúde PB

## 📌 Sobre o Projeto

O **Acesso Saúde PB** é uma aplicação desenvolvida para facilitar a consulta de unidades de saúde da Paraíba a partir dos dados do CNES (Cadastro Nacional de Estabelecimentos de Saúde).

A aplicação permite pesquisar unidades de saúde utilizando filtros como:

- Cidade
- Bairro
- Tipo de unidade
- Turno de atendimento
- Nome da unidade

Além disso, também é possível visualizar:

- Informações da unidade
- Endereço
- Capacidades da unidade
- Profissionais vinculados

---

# 🚀 Tecnologias Utilizadas

## Backend

- Java 21
- Spring Boot
- Spring Data JPA
- Hibernate
- PostgreSQL
- Maven

## Frontend

- HTML5
- CSS3
- JavaScript

## Scripts de Dados

- Python
- Pandas
- SQLAlchemy

---

# 📁 Estrutura do Projeto

```text
acesso-saude-pb/
│
├── src/                     # Aplicação Spring Boot
│
├── scripts/                 # Scripts Python de tratamento e carregamento de dados
│
├── pom.xml
├── mvnw
├── mvnw.cmd
└── README.md
```

---

# 🗄️ Banco de Dados

A aplicação utiliza PostgreSQL como banco de dados.

## Tabelas

- `tb_unidades`
- `tb_enderecos`
- `tb_cidades`
- `tb_turnos`
- `tb_tipos_unidade`
- `tb_capacidades`
- `tb_profissionais`
- `tb_profissional_unidade`

---

# ▶️ Executando os Scripts Python

Os scripts responsáveis pela limpeza e carga dos dados estão na pasta:

```text
scripts/
```
---

# 🔎 Funcionalidades

- Consulta de unidades de saúde
- Filtro por cidade
- Filtro por bairro
- Filtro por tipo de unidade
- Filtro por turno
- Busca por nome da unidade
- Exibição de capacidades da unidade
- Exibição de profissionais vinculados

---

# 📚 Fonte dos Dados

Os dados utilizados foram obtidos a partir do CNES:

- Cadastro Nacional de Estabelecimentos de Saúde
- DATASUS

---

# 👩‍💻 Autors

Desenvolvido por Annaely Oliveira, Andrey Rian e Adson Ruan.
