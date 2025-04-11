# MinSORTING - Aplicação de Simulação de Distribuição Granulométrica

## Visão Geral

MinSORTING é uma aplicação web para simulação de distribuição granulométrica de minerais detríticos. A aplicação é baseada no artigo de Resentini et al. (2013) [Computers & Geosciences 59 (2013) 90-97] e permite aos usuários modelar a distribuição de minerais em sedimentos com base em diferentes parâmetros.

## Funcionalidades Principais

- Simulação de distribuição granulométrica para diferentes tipos de minerais
- Suporte para diferentes tipos de fluidos (água doce, água do mar, ar)
- Modelagem de diferentes proveniências de sedimentos
- Visualização de resultados através de gráficos interativos
- Exportação de resultados para formato CSV

## Arquitetura da Aplicação

A aplicação é composta pelos seguintes componentes principais:

### 1. Aplicação Principal

- `index()`: Renderiza a página inicial com o formulário de entrada
- `calculate()`: Processa os dados do formulário e calcula os resultados
- `export_csv()`: Exporta os resultados como arquivo CSV

### 2. `calculations.py` - Lógica de Cálculo

Contém as funções matemáticas para calcular a distribuição granulométrica:

- `calculate_bulk_density()`: Calcula a densidade bulk do sedimento
- `get_settling_equations()`: Seleciona as equações apropriadas baseado no tipo de fluido
- `calculate_mineral_distribution()`: Calcula a distribuição granulométrica para cada mineral
- `generate_plots()`: Gera gráficos Plotly para visualização dos resultados

### 3. `data_store.py` - Armazenamento de Dados

Contém as constantes e dados utilizados pela aplicação:

- Propriedades dos fluidos (densidade, viscosidade)
- Propriedades dos minerais (densidade padrão, mínima, máxima)
- Composições de proveniência
- Constantes físicas (gravidade, conversões phi-mm)

## Como Usar a Aplicação

### 1. Inserindo Dados

Na página inicial, você pode inserir os seguintes parâmetros:

- **Diâmetro Médio (dm)**: Diâmetro médio em phi
- **Sorting (sigma)**: Desvio padrão em phi
- **Tipo de Fluido**: Água doce, água do mar ou ar
- **Proveniência**: Tipo de proveniência do sedimento
- **Opção de Densidade**: Padrão ou ajuste fino

### 2. Visualizando Resultados

Após submeter o formulário, a aplicação exibirá:

- Uma tabela com a distribuição granulométrica para cada mineral
- Gráficos interativos mostrando a distribuição cumulativa
- Opção para exportar os resultados como CSV

### 3. Exportando Resultados

Para exportar os resultados como arquivo CSV, clique no botão "Exportar CSV" na página de resultados.

## Dependências

A aplicação utiliza as seguintes bibliotecas Python:

- Pandas: Manipulação de dados
- NumPy: Cálculos numéricos
- SciPy: Funções estatísticas
- Plotly: Geração de gráficos interativos

## Referências

RESENTINI, Alberto; MALUSÀ, Marco G.; GARZANTI, Eduardo. MinSORTING: An Excel® worksheet for modelling mineral grain-size distribution in sediments, with application to detrital geochronology and provenance studies. Computers & Geosciences, v. 59, p. 90-97, 2013

MALUSÀ, Marco G.; RESENTINI, Alberto; GARZANTI, Eduardo. Hydraulic sorting and mineral fertility bias in detrital geochronology. Gondwana Research, v. 31, p. 1-19, 2016.

## Licença

Este projeto está licenciado sob a licença MIT 
