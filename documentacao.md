# Documentação do Código

Este script utiliza a biblioteca `selenium` para automatizar a extração de dados de vendas de jogos do site "SteamDB". O script navega pela página de vendas, coleta informações específicas sobre os jogos em promoção e salva esses dados em um arquivo CSV.

## Dependências

- `selenium`: Para automatizar a navegação na web e a extração de dados.
- `webdriver`: Para controlar o navegador Chrome.

## Configuração Inicial

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
```

## Inicialização do WebDriver

Configura o serviço e as opções do Chrome para iniciar o WebDriver.

```python
servico = Service()
opcoes = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=servico, options=opcoes)
```

## Navegação para a URL Alvo

Define a URL da página de vendas do SteamDB e navega até ela.

```python
url = "https://steamdb.info/sales/"
driver.get(url)
```

## Definição de Variáveis

Define as variáveis para armazenar os dados coletados e especifica a quantidade de jogos e páginas a serem processadas.

```python
quantidade_de_jogos = 101
quantidade_de_paginas = 4
nomes = []
precos = []
avaliacoes = []
datas_lancamento = []
datas_experira_desconto = []
datas_comeco_desconto = []
```

## Loop Principal de Coleta de Dados

O loop principal itera sobre o número de páginas especificadas e coleta os dados de cada jogo listado.

### Scroll na Página

Executa o scroll na página para carregar os elementos dinâmicos.

```python
for i in range(quantidade_de_paginas):
    for i in range(10):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(0.25)
    driver.execute_script("window.scrollBy(0, -900);")
```

### Coleta de Dados

Para cada jogo na página, coleta nome, preço, avaliação, data de lançamento, data de expiração do desconto e data de início do desconto.

```python
for i in range(1, quantidade_de_jogos):
    nome_xpath = f"/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[3]/a"
    nome_elemento = driver.find_element(By.XPATH, nome_xpath)
    nomes.append(nome_elemento.text.replace(",", "."))
    
    preco_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[5]"
    preco_elemento = driver.find_element(By.XPATH, preco_xpath)
    precos.append(preco_elemento.text.replace(",", "."))
    
    avaliacao_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[6]"
    avaliacao_elemento = driver.find_element(By.XPATH, avaliacao_xpath)
    avaliacoes.append(avaliacao_elemento.text)
    
    data_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[7]"
    data_elemento = driver.find_element(By.XPATH, data_xpath)
    datas_lancamento.append(data_elemento.text)
    
    data_expiraca_desconto_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[8]"
    data_expiraca_desconto_elemento = driver.find_element(By.XPATH, data_expiraca_desconto_xpath)
    datas_experira_desconto.append(data_expiraca_desconto_elemento.get_attribute("title")[:11])
    
    data_comeco_desconto_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[9]"
    data_comeco_desconto_elemento = driver.find_element(By.XPATH, data_comeco_desconto_xpath)
    datas_comeco_desconto.append(data_comeco_desconto_elemento.get_attribute("title")[:11])
```

### Navegação para a Próxima Página

Após coletar os dados de uma página, navega para a próxima página.

```python
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div[2]/button[8]").click()
time.sleep(10)
```

## Salvamento dos Dados em CSV

Após coletar todos os dados, salva-os em um arquivo CSV.

```python
with open("dados.csv", "w", encoding="utf-8") as arq:
    arq.write("NOME,PRECO,AVALIACAO,DATA_LANCAMENTO,DATA_EXPIRA_DESCONTO,DATA_COMECA_DESCONTO\n")
    for nome, preco, avaliacao, data_lancamento, expira, comeca in zip(nomes, precos, avaliacoes, datas_lancamento, datas_experira_desconto, datas_comeco_desconto):
        arq.write(nome + "," + preco + "," + avaliacao + "," + data_lancamento + "," + expira + "," + comeca + "\n")
```

## Observações

- Não foi possível fazer a consulta em todas as páginas, pois o código apresentava problemas a partir da quinta página, não consegui solucionar o problema.
- Por conta da falta de tempo não consegui adicionar informações adicionais ao arquivo, como desenvolvedor do jogo, publisher e outras informações, com um tempo a mais, seria possível adicionar essas informações.
- link do google planilha: https://docs.google.com/spreadsheets/d/1f_aWcZYKZ9aRAMi4_jzUZCGStEDpJDDwx9I0wssN8-I/edit?usp=sharing