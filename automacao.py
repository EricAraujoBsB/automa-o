from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# abrir o navegador

navegador = webdriver.Chrome()

# acessar site

navegador.get("https://www.hashtagtreinamentos.com/")

# colocar em tela cheia

navegador.maximize_window()

#selecionar um elemento 

botao_verde = navegador.find_element("class name", "botao-verde")

navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_verde)

espera = WebDriverWait(navegador, 10)
espera.until(ec.element_to_be_clickable(botao_verde))

botao_verde.click()

# selecionar uma aba

abas = navegador.window_handles
navegador.switch_to.window(abas[1])

navegador.get("https://www.hashtagtreinamentos.com/curso-python?utm_source=site&utm_medium=header&utm_content=link-header-cursos&utm_campaign=programacao&conversion=lcto-lpy24-set25")


# escrever um formulário
campo_nome = navegador.find_element("id", "firstname")
campo_nome.send_keys("eric")
campo_email = navegador.find_element("id", "email")
campo_email.send_keys("aokfmovan@ofn.com")
campo_phone = navegador.find_element("id", "phone")
campo_phone.send_keys("651555555555")

botao_assinatura = navegador.find_element("id", "_form_2475_submit")
# scrool
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_assinatura)

espera = WebDriverWait(navegador, 10)
espera.until(ec.element_to_be_clickable(botao_assinatura))

botao_assinatura.click()


time.sleep(10)
