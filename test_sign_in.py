# 1 - Bibliotecas
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe
class Test_SignIn():
    
    # 2.1 - Atributos
    url = "https://www.giulianaflores.com.br/" 

    # 2.2 - Funcoes e metodos
    def setup_method(self,method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self,method):
        self.driver.quit()

    def test_sign_in(self):
        self.driver.get(self.url)
        self.driver.set_window_size(1382, 754)
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
        self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Oliver Fernando Vicente Pereira")
        self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("615.249.658-63")
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("oliver.fernando.pereira@expressotaubate.com.br")
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("QE2KOghkBj")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("09169-206")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_btnAddressFind").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("442")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("11985278293")
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()