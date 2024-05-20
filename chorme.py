from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servico = Service()

opcoes = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=servico, options=opcoes)

url = "https://steamdb.info/sales/"

driver.get(url)

quantidade_de_jogos = 101
quantidade_de_paginas = 4
nomes = []
precos = []
avaliacoes = []
datas_lancamento = []
datas_experira_desconto = []
datas_comeco_desconto = []

for i in range(quantidade_de_paginas):

    for i in range(10):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(0.25)

    driver.execute_script("window.scrollBy(0, -900);")

    
    for i in range(1, quantidade_de_jogos):
        nome_xpath = f"/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/table/tbody/tr[{i}]/td[3]/a"
        nome_elemento = driver.find_element(By.XPATH, nome_xpath)
        nomes.append(nome_elemento.text.replace(",","."))

    
    for i in range(1, quantidade_de_jogos):
        preco_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[5]"
        preco_elemento = driver.find_element(By.XPATH, preco_xpath)
        precos.append(preco_elemento.text.replace(",","."))

    
    for i in range(1, quantidade_de_jogos):
        avaliacao_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[6]"
        avaliacao_elemento = driver.find_element(By.XPATH, avaliacao_xpath)
        avaliacoes.append(avaliacao_elemento.text)

    
    for i in range(1, quantidade_de_jogos):
        data_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[7]"
        data_elemento = driver.find_element(By.XPATH, data_xpath)
        datas_lancamento.append(data_elemento.text)

    
    for i in range(1, quantidade_de_jogos):
        data_expiraca_desconto_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[8]"
        data_expiraca_desconto_elemento = driver.find_element(By.XPATH, data_expiraca_desconto_xpath)
        datas_experira_desconto.append(data_expiraca_desconto_elemento.get_attribute("title")[:11])

    
    for i in range(1, quantidade_de_jogos):
        data_comeco_desconto_xpath = f"//*[@id='DataTables_Table_0']/tbody/tr[{i}]/td[9]"
        data_comeco_desconto_elemento = driver.find_element(By.XPATH, data_comeco_desconto_xpath)
        datas_comeco_desconto.append(data_comeco_desconto_elemento.get_attribute("title")[:11])

    time.sleep(10)

    driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[3]/div[2]/button[8]").click()

    time.sleep(10)
    
with open("dados.csv", "w", encoding="utf-8") as arq:
    arq.write("NOME,PRECO,AVALIACAO,DATA_LANCAMENTO,DATA_EXPIRA_DESCONTO,DATA_COMECA_DESCONTO\n")
    for nome, preco, avaliacao, data_lancamento, expira, comeca in zip(nomes, precos, avaliacoes, datas_lancamento, datas_experira_desconto, datas_comeco_desconto):
        arq.write(nome + "," + preco + "," + avaliacao + "," + data_lancamento + "," + expira + "," + comeca +"\n")
