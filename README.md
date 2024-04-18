# Projeto de Análise de Dados

Este projeto implementa uma análise de dados exploratória usando Python, focando na transformação, visualização e regressão linear de conjuntos de dados. Utilizamos bibliotecas como `pandas`, `matplotlib`, `numpy`, e `scipy` para manipulação de dados e geração de visualizações gráficas.

## Estrutura do Projeto

A classe `DataAnalysis` é o núcleo deste projeto, permitindo o carregamento, transformação, visualização e análise estatística de dados extraídos de arquivos CSV. As principais funcionalidades incluem:

### Métodos da Classe `DataAnalysis`

-   **`__init__(self, filename)`:** Construtor que carrega os dados do arquivo CSV especificado.
-   **`transform_data(self, x, y)`:** Recebe os nomes das colunas `x` e `y` e transforma esses dados para suas formas logarítmicas.
-   **`plot_data(self)`:** Gera e salva um gráfico dos dados originais (`x` vs `y`) usando pontos azuis.
-   **`plot_data_log(self)`:** Gera e salva um gráfico dos dados transformados em logaritmo (`ln(x)` vs `ln(y)`).
-   **`linear_regression(self)`:** Realiza uma regressão linear nos dados logarítmicos, plotando os dados, a linha de ajuste, e os erros residuais. Calcula e exibe a inclinação, intercepto, e R².
-   **`linear_regression_no_intercept(self)`:** Similar ao método de regressão linear, mas força o intercepto a zero. Exibe a inclinação e R² calculados.

## Dependências

Para rodar este projeto, você precisa instalar as seguintes bibliotecas Python:

-   pandas
-   matplotlib
-   numpy
-   scipy

Você pode instalar todas as dependências necessárias utilizando o seguinte comando pip:

bashCopy code

`pip install pandas matplotlib numpy scipy` 

## Como Usar

1.  **Clonar o Repositório**
    
    Primeiro, clone o repositório para sua máquina local usando:
    ```bash
    git clone git@github.com:GustavoGarciaPereira/DataLogAnalysis.git
    ```
    
2.  **Carregando e Analisando os Dados**
    
    No seu script Python, crie uma instância da classe `DataAnalysis` com o caminho do seu arquivo CSV:
    
    
    ```python
    from data_analysis import DataAnalysis
    
    # Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo de dados
    analysis = DataAnalysis('seu_arquivo.csv')
    ```
    
    
3.  **Executando Análises**
    
    Você pode executar diversas análises e visualizações:
    
    ```python
    # Substitua 'coluna_x' e 'coluna_y' pelos nomes das colunas dos seus dados
    analysis.transform_data('coluna_x', 'coluna_y')
    analysis.plot_data()
    analysis.plot_data_log()
    analysis.linear_regression()
    analysis.linear_regression_no_intercept()
    # DataLogAnalysis
    ```
