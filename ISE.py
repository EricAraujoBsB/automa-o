from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

navegador = webdriver.Chrome()
navegador.maximize_window()

navegador.get("https://10.2.140.101/admin/login.jsp")


campo_user = navegador.find_element("id", "user")
campo_user.send_keys("eric.araujo")

campo_senha = navegador.find_element("id", "password")
campo_senha.send_keys("91931204$Bv")




time.sleep(20)