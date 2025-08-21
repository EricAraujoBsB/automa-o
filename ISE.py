from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data.operacoes import inserir_dados_bd

def teste_conexao(value):
    try:
        inserir_dados_bd(value)
        print("Valor enviado com sucesso")
    except Exception as error:
        print("Falha ao comunicar com banco de dados")

# Função de automação
def automacao():
    navegador = webdriver.Chrome()

    navegador.get("https://10.2.140.101/admin/login.jsp")
    navegador.maximize_window()
    time.sleep(3)

    campo_user = navegador.find_element("id", "dijit_form_TextBox_0")
    campo_user.send_keys("eric.araujo")

    campo_senha = navegador.find_element("id", "dijit_form_TextBox_1")
    campo_senha.send_keys("91931204$Bv")

    login = navegador.find_element("id", "loginPage_loginSubmit")
    login.click()

    time.sleep(5)

    lista_titulos = navegador.find_elements("class name", "dashlet-title")
    lista_values = navegador.find_elements("class name", "metric-value ")

    # espera = WebDriverWait(navegador, 10)
    # espera.until(ec.presence_of_element_located(lista_titulos))
    # try:
    #     while True:
    #         try:
    #             for titulo, value in zip(lista_titulos, lista_values):
    #                 if titulo.text == "Active Endpoints":
    #                     active_endpoints_value = int(value.text)
    #                     print(active_endpoints_value)
    #                 break
                
    #         except Exception as e:
    #             print(f"Erro ao tentar encontrar o elemento: {e}")
    #         time.sleep(60)

    # except KeyboardInterrupt:
    #     print("Monitoramento interrompido pelo usuário.")
    
    for titulo, value in zip(lista_titulos, lista_values):
        if titulo.text == "Active Endpoints":
            active_endpoints_value = int(value.text)
            print(active_endpoints_value)

            break  # Para o loop quando encontrar o segundo "Active Endpoints"
    
    time.sleep(10)

# Chama a função de automação
# automacao()

value = 65915
teste_conexao(value)

