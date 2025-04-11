# Documentação Técnica - MinSORTING

## Visão Geral da Arquitetura

A aplicação MinSORTING é uma aplicação web Flask que implementa um modelo matemático para simulação de distribuição granulométrica de minerais detríticos em sedimentos. A arquitetura segue um padrão MVC (Model-View-Controller) simplificado, com separação clara entre lógica de negócios, dados e interface do usuário.

## Componentes Principais

### 1. Controlador (`app.py`)

O controlador gerencia as requisições HTTP e coordena a interação entre o modelo e a visualização.

#### Funções Principais:

- **`index()`**: Rota GET para a página inicial
  - Renderiza o template `index.html`
  - Passa as propriedades dos minerais e composições de proveniência para o template

- **`calculate()`**: Rota POST para processamento do formulário
  - Recupera e valida os dados do formulário
  - Chama as funções de cálculo do modelo
  - Armazena os parâmetros de entrada na sessão
  - Renderiza o template `results.html` com os resultados

- **`export_csv()`**: Rota GET para exportação de dados
  - Recupera os parâmetros da sessão
  - Recalcula o DataFrame com os parâmetros armazenados
  - Gera e retorna um arquivo CSV

### 2. Modelo

O modelo é composto por dois módulos principais:

#### 2.1. Armazenamento de Dados (`data_store.py`)

Contém todas as constantes e dados estáticos utilizados pela aplicação:

- **`FLUID_PROPERTIES`**: Dicionário com propriedades dos fluidos
  - Chaves: "Freshwater", "Seawater", "Air"
  - Valores: Dicionários com "density" e "viscosity"

- **`MINERAL_PROPERTIES`**: Dicionário com propriedades dos minerais
  - Chaves: Abreviações dos minerais (ex: "Q", "F", "Zrn")
  - Valores: Dicionários com "name", "standard_density", "min_density", "max_density", "calc_density"

- **`PROVENANCE_COMPOSITIONS`**: Dicionário com composições de proveniência
  - Chaves: Nomes das proveniências
  - Valores: Dicionários com porcentagens de cada mineral

- **Constantes Físicas**:
  - `GRAVITY`: Aceleração da gravidade (9.81 m/s²)
  - `PHI_TO_MM`: Função lambda para converter phi para mm
  - `MM_TO_PHI`: Função lambda para converter mm para phi

#### 2.2. Lógica de Cálculo (`calculations.py`)

Implementa as funções matemáticas para calcular a distribuição granulométrica:

- **`calculate_bulk_density()`**: Calcula a densidade bulk do sedimento
  - Entrada: Composição da proveniência e densidades de cálculo
  - Saída: Densidade bulk em g/cm³

- **`get_settling_equations()`**: Seleciona as equações apropriadas baseado no tipo de fluido
  - Entrada: Tipo de fluido e diâmetro médio
  - Saída: Funções para calcular velocidade de decantação e size-shift

- **`calculate_mineral_distribution()`**: Calcula a distribuição granulométrica para cada mineral
  - Entrada: Parâmetros do sedimento (dm, sigma, fluid_type, provenance_name)
  - Saída: DataFrame com a distribuição granulométrica

- **`generate_plots()`**: Gera gráficos Plotly para visualização dos resultados
  - Entrada: DataFrame com os resultados
  - Saída: Dicionário com os gráficos em formato JSON

### 3. Visualização (Templates)

Os templates HTML são renderizados pelo Flask e exibem a interface do usuário:

- **`index.html`**: Formulário de entrada com os parâmetros da simulação
- **`results.html`**: Exibição dos resultados, incluindo tabelas e gráficos

## Fluxo de Dados

1. O usuário acessa a página inicial (`/`)
2. O usuário preenche o formulário e o envia (POST `/`)
3. O controlador processa os dados e chama as funções de cálculo
4. Os resultados são armazenados na sessão e exibidos ao usuário
5. O usuário pode exportar os resultados como CSV (`/export_csv`)

## Gerenciamento de Estado

A aplicação utiliza a sessão do Flask para armazenar os parâmetros de entrada entre requisições. Isso permite que o usuário exporte os resultados sem precisar recalcular manualmente.

## Tratamento de Erros

A aplicação implementa tratamento de erros em vários níveis:

1. **Validação de Entrada**: Verifica se os dados do formulário são válidos
2. **Tratamento de Exceções**: Captura e exibe erros de forma amigável
3. **Verificação de Sessão**: Verifica se os dados necessários estão disponíveis na sessão

## Considerações de Desempenho

- A aplicação recalcula o DataFrame a cada exportação para evitar armazenar dados grandes na sessão
- Os gráficos são gerados apenas quando necessário
- As constantes e dados estáticos são carregados uma única vez na inicialização

## Extensibilidade

A aplicação foi projetada para ser facilmente extensível:

- Novos tipos de fluidos podem ser adicionados ao dicionário `FLUID_PROPERTIES`
- Novos minerais podem ser adicionados ao dicionário `MINERAL_PROPERTIES`
- Novas proveniências podem ser adicionadas ao dicionário `PROVENANCE_COMPOSITIONS`
- Novas equações de decantação podem ser implementadas na função `get_settling_equations()`

## Referências

RESENTINI, Alberto; MALUSÀ, Marco G.; GARZANTI, Eduardo. MinSORTING: An Excel® worksheet for modelling mineral grain-size distribution in sediments, with application to detrital geochronology and provenance studies. Computers & Geosciences, v. 59, p. 90-97, 2013.
