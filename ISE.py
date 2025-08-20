from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pathlib import Path

current_dir = Path(__file__).parent

from data.conexao import inserir_valor_bd


navegador = webdriver.Chrome()
navegador.maximize_window()

navegador.get("https://10.2.140.101/admin/login.jsp")


karspesky = navegador.find_element("id", "karspersky").click()


campo_user = navegador.find_element("id", "user")
campo_user.send_keys("eric.araujo")

campo_senha = navegador.find_element("id", "password")
campo_senha.send_keys("*************$Bv")

login = navegador.find_element("class name", "login").click()


try:
    while True:
        try:
            # Tentando localizar o elemento
            elemento = navegador.find_element("class name", "activate-endpoints")
            atual = elemento.text
            if atual is not None:
                try:
                    inserir_valor_bd()
            else:

            # Aqui você pode adicionar qualquer lógica para lidar com o estado do elemento
            if elemento.is_displayed():
                print("Elemento encontrado e visível!")
            else:
                print("Elemento encontrado, mas não está visível.")
        except Exception as e:
            print(f"Erro ao tentar encontrar o elemento: {e}")

        # Aguarda 1 minuto antes de verificar novamente
        time.sleep(60)

except KeyboardInterrupt:
    print("Monitoramento interrompido pelo usuário.")

finally:
    # Fechar o driver após o término do monitoramento
    driver.quit()




time.sleep(20)