# 1 - Bibliotecas
import pytest
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe
class Test_LoginNeg():
    
    # 2.1 - Atributos
    url = "https://www.giulianaflores.com.br/" 

    # 2.2 - Funcoes e metodos
    def setup_method(self,method):
        self.driver = webdriver.Chrome()   #recebe/instancia o objeto do Selenium WebDriver como Chrome
        self.driver.implicitly_wait(10)

    def teardown_method(self,method):
        self.driver.quit()

    def test_login_neg(self):
        name = 'oliver.fernando@expressotaubate.com.br'
        password = 'QE2KOghkBj'

        self.driver.get(self.url)
        self.driver.set_window_size(1382, 754)
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(name)
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys(password)
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        time.sleep(10)
        assert self.driver.find_element(By.CSS_SELECTOR, ".aviso-erro").text == 'ATENÇÃO - e-mail ou senha inválidos!'