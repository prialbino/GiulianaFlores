# 1 - Bibliotecas
import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe
class Test_FluxoCompra():
    
    # 2.1 - Atributos
    url = "https://www.giulianaflores.com.br/" 

    # 2.2 - Funcoes e metodos
    def setup_method(self,method):
        self.driver = webdriver.Chrome()   #recebe/instancia o objeto do Selenium WebDriver como Chrome
        self.driver.implicitly_wait(10)

    def teardown_method(self,method):
        self.driver.quit()

    def test_fluxo_compra(self):
        name = 'oliver.fernando.pereira@expressotaubate.com.br'
        password = 'QE2KOghkBj'

        self.driver.get(self.url)
        self.driver.set_window_size(1382, 754)
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(name)
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys(password)
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "txtDsKeyWord").send_keys("orquideas")
        self.driver.find_element(By.ID, "btnSearch").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "div.close-button").click()
    
        self.driver.find_element(By.CSS_SELECTOR,'li.item[data-idproductline="141"] > div.product-item > a[data-idproduct="31138"]').click()

        assert self.driver.find_element(By.ID,"ContentSite_lblProductDsName").text == "Mini Orquídea Rara Amarela"
        assert self.driver.find_element(By.CSS_SELECTOR, "precoPor_prod").text == "R$ 99,90"
        self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
        self.driver.find_element(By.ID, "ContentSite_uwcCalendar_txtZip").send_keys("09169")
        self.driver.find_element(By.ID, "ContentSite_uwcCalendar_txtZipComplement").send_keys("206")
        self.driver.find_element(By.CSS_SELECTOR, "span.btn_okcep.jSelectZip").click()
        self.driver.find_element(By.CSS_SELECTOR, "a.selectDate").click()
        self.driver.find_element(By.CSS_SELECTOR, ".box_periodos > ul:nth-child(3) > li:nth-child(3) > input:nth-child(1)").click()
        self.driver.find_element(By.ID, "btConfirmShippingData").click()
        self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
        self.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click()
        self.driver.find_element(By.ID, "txtDsDestinationName").send_keys("Maria da Silva")
        self.driver.find_element(By.ID, "txtPhone").send_keys(11984568811)
        self.driver.find_element(By.ID, "ContentSite_rptDeliveryAddress_rbtFgPersonalAddress_0_0_0").click()
        self.driver.find_element(By.ID, "txtDsNumber").send_keys("100")
        self.driver.find_element(By.ID, "rbWhithoutGiftCard").click()
        self.driver.find_element(By.ID, "btnContinue").click()
        self.driver.find_element(By.ID, "ContentSite_spanCartao").click()
        self.driver.find_element(By.ID, "ContentSite_tbxOPDDsCardNumber").send_keys("5251308607428754")
        self.driver.find_element(By.ID, "ContentSite_tbxOPDDsCardOwner").send_keys("Joana Silva")
        self.driver.find_element(By.ID, "ContentSite_ddlOPDDsCardMonthExpires").send_keys("Julho")
        self.driver.find_element(By.ID, "ContentSite_ddlOPDDsCardYearExpires").send_keys("2025")
        self.driver.find_element(By.ID, "ContentSite_tbxOPDDsCardComp").send_keys("566")
        self.driver.find_element(By.CSS_SELECTOR, '#rbtParcelSelected\,10 > option:nth-child(1)').click()
        self.driver.find_element(By.ID, "ContentSite_ibtFinalizeOrderWithCreditCard").click()
        self.driver.find_element(By.CSS_SELECTOR, ".logo_checkout > a:nth-child(1) > img:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bg_carrinho > img:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bt_finalizar_carrinho_suspenso_header").click()
        self.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_rptBasketItems_0_lbtRemoveProduct_0").click()
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "pLogOutFace").click()
