from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from data.operacoes import inserir_dados_bd


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

time.sleep(10)
btn_carrosel = navegador.find_element("id", "carousel-next")
espera = WebDriverWait(navegador, 20)
espera.until(ec.element_to_be_clickable(btn_carrosel))

btn_carrosel.click()
time.sleep(2)
btn_carrosel.click()
time.sleep(2)
btn_carrosel.click()
time.sleep(2)
btn_carrosel.click()
time.sleep(2)

lista_titulos = navegador.find_elements("class name", "dashlet-title")
lista_values = navegador.find_elements("class name", "metric-value ")

for titulo in lista_titulos:
    for value in lista_values:

        print(titulo.text)

        titulo_activate = titulo.text
        if titulo_activate == "Active Endpoints":
            value_actual = value.text
            print(value_actual)
            time.sleep(5)
        break
        # else:
        #     print("activate endpoint não localizado")


# try:
#     while True:
#         try:
#             Activate = navegador.find_element()

time.sleep(10)