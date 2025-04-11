# Guia do Usuário - MinSORTING

## Introdução

O MinSORTING é uma aplicação web para simulação de distribuição granulométrica de minerais detríticos em sedimentos. Este guia fornece instruções detalhadas sobre como usar a aplicação, interpretar os resultados e exportar os dados para análise posterior.

## Acessando a Aplicação

1. Inicie o servidor Flask executando o comando `python app.py` no terminal
2. Abra seu navegador e acesse `http://127.0.0.1:5000`
3. A página inicial será exibida com o formulário de entrada

## Preenchendo o Formulário

### Parâmetros Básicos

- **Diâmetro Médio (dm)**: 
  - Valor em phi (φ)
  - Representa o tamanho médio dos grãos do sedimento
  - Valores típicos: entre -2 e 4 phi

- **Sorting (sigma)**: 
  - Valor em phi (φ)
  - Representa o desvio padrão da distribuição granulométrica
  - Valores típicos: entre 0.5 e 2 phi

- **Tipo de Fluido**: 
  - **Água Doce**: Para sedimentos em ambientes fluviais ou lacustres
  - **Água do Mar**: Para sedimentos em ambientes marinhos
  - **Ar**: Para sedimentos em ambientes eólicos

- **Proveniência**: 
  - Selecione a proveniência do sedimento
  - Cada proveniência tem uma composição mineralógica específica
  - Opções incluem: Arco Magmático Indissectado, Arco Magmático Dissectado, Ofiolito, etc.

### Opções Avançadas

- **Opção de Densidade**: 
  - **Padrão**: Usa as densidades padrão dos minerais
  - **Ajuste Fino**: Permite ajustar as densidades dos minerais individualmente

- **Ajuste Fino de Densidades** (apenas quando "Ajuste Fino" é selecionado):
  - Campos de entrada para cada mineral
  - Permite ajustar a densidade de cálculo para cada mineral
  - Valores devem estar entre a densidade mínima e máxima do mineral

## Interpretando os Resultados

### Tabela de Distribuição Granulométrica

A tabela mostra a distribuição granulométrica para cada mineral:

- **Linhas**: Intervalos de phi (φ)
- **Colunas**: Minerais individuais e total
- **Valores**: Porcentagem de cada mineral em cada intervalo de phi
- **Última linha**: Total para cada mineral

### Gráficos

A aplicação gera dois tipos de gráficos:

1. **Distribuição Cumulativa**:
   - Eixo X: Tamanho em phi (φ)
   - Eixo Y: Porcentagem cumulativa
   - Linhas: Minerais principais (Quartzo, Feldspato, Zircão, Granada) e sedimento total
   - Útil para comparar a distribuição de diferentes minerais

2. **Distribuição de Frequência**:
   - Eixo X: Tamanho em phi (φ)
   - Eixo Y: Porcentagem em cada intervalo
   - Barras: Distribuição de frequência para cada mineral
   - Útil para visualizar a distribuição modal

### Interpretação dos Gráficos

- **Curvas mais à direita**: Minerais mais leves (ex: Quartzo, Feldspato)
- **Curvas mais à esquerda**: Minerais mais pesados (ex: Zircão, Granada)
- **Curvas mais íngremes**: Melhor seleção (sorting)
- **Curvas mais suaves**: Pior seleção (sorting)

## Exportando os Dados

Para exportar os resultados como arquivo CSV:

1. Na página de resultados, clique no botão "Exportar CSV"
2. O arquivo será baixado automaticamente
3. O arquivo CSV contém a mesma informação da tabela de resultados
4. Você pode abrir o arquivo em Excel, Google Sheets ou qualquer outro programa de planilhas

## Dicas e Truques

### Seleção de Parâmetros

- **Para sedimentos bem selecionados**: Use valores baixos de sigma (0.5-1 phi)
- **Para sedimentos mal selecionados**: Use valores altos de sigma (1.5-2 phi)
- **Para grãos grossos**: Use valores negativos de dm (-2 a 0 phi)
- **Para grãos finos**: Use valores positivos de dm (2 a 4 phi)

### Interpretação de Resultados

- **Comparação com dados reais**: Compare os resultados com dados de amostras reais
- **Análise de proveniência**: Use diferentes proveniências para entender a origem do sedimento
- **Efeito do fluido**: Compare resultados com diferentes tipos de fluido para entender o efeito do ambiente de deposição

## Solução de Problemas

### Erros Comuns

- **"Nenhum resultado disponível para exportação"**: Você precisa calcular os resultados antes de exportar
- **"Valor inválido"**: Verifique se os valores inseridos estão dentro dos intervalos recomendados
- **"Erro de cálculo"**: Verifique se todos os campos obrigatórios foram preenchidos

### Limitações

- A aplicação assume uma distribuição normal (gaussiana) para cada mineral
- Não considera efeitos de forma dos grãos
- Não considera efeitos de concentração de partículas

## Referências

Para mais informações sobre o modelo matemático e suas aplicações, consulte:

Resentini, A., Andò, S., Vezzoli, G., Garzanti, E., 2013. MinSORTING: An Excel worksheet for modelling mineral grain-size distribution in sediments, with application to detrital geochronology and provenance studies. Computers & Geosciences 59, 90-97. 