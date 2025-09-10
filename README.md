# Dashboard IoT - Streamlit + ClickHouse

## Descrição

Este projeto é um **dashboard interativo de dados de temperatura de dispositivos IoT**, desenvolvido com Streamlit, Plotly e ClickHouse. Os dados são carregados a partir de um CSV e armazenados em um banco ClickHouse, possibilitando consultas rápidas e visualizações em tempo real.

---

## Funcionalidades

- Inserção de dados a partir de arquivo CSV (`temperature.csv`).
- Gráficos interativos com Plotly:
  - Temperatura média por dispositivo.
  - Quantidade de leituras por hora.
  - Temperatura máxima e mínima por hora.
- Dashboard em Streamlit acessível pelo navegador.
- Atualização dos gráficos em tempo real a cada execução.

---

## Tecnologias usadas

- Python
- Streamlit
- Plotly
- Pandas
- ClickHouse
- Docker & Docker Compose

---

## Pré-requisitos

- Docker e Docker Compose
- Python 3.11+ 
- Dependências Python do arquivo `requirements.txt`

---

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/Menezes-D/Portfolio_DisruptiveArchitectures.git
cd pipeline-iot
```

2. Suba o container ClickHouse com Docker Compose:

```bash
docker-compose up -d
```

3. Instale as dependências Python:

```bash
pip install -r requirements.txt
```

4. Abra o terminal na pasta src e execute o dashboard

```bash
streamlit run main.py
```

---

5. Abra o navegador na URL exibida pelo Streamlit

```bash
(geralmente http://localhost:8501)
```
---

## ESTRUTURA DO PROJETO

```bash
├── docker
│   ├── data
│   │   └── temperature.csv       # Arquivo CSV com dados de temperatura
│   └── docker-compose.yml        # Configuração do container ClickHouse
├── src
│   └── main.py                   # Dashboard Streamlit
├── requirements.txt              # Dependências Python
└── README.md
```
---

## Funcionamento da Visualização

- Temperatura média por dispositivo: mostra um gráfico de barras com a média de cada dispositivo.

- Leituras registradas por hora: exibe quantas leituras foram registradas em cada hora do dia.

- Variação de temperatura máxima e mínima por hora: gráfico de linhas com múltiplas séries para analisar variações ao longo do dia.

- Os dados devem estar no CSV localizado em docker/data/temperature.csv.

- Ao rodar o main.py, o dashboard se conecta ao ClickHouse e realiza consultas SQL para gerar os gráficos.

---

## Conexão com os conceitos aprendidos

- Este projeto integra os seguintes conceitos:

- Criação e manipulação de bancos de dados analíticos ClickHouse.

- Consumo de dados com Pandas.

- Visualização interativa de dados com Plotly.

- Criação de dashboards responsivos com Streamlit.

- Containerização de serviços e persistência de dados usando Docker e Docker Compose.

---
