import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I access the Giuliana Flores website')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.giulianaflores.com.br/") 

@when(u'I click in the login button')
def step_impl(context):
    context.driver.find_element(By.ID, "perfil-hidden").click()
    time.sleep(5)
    context.driver.find_element(By.ID, "UrlLogin").click() 


@when(u'I inform all the mandatory information for the new sign up')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
    context.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Emanuel Luís Isaac Campos")
    context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("312.801.101-04")
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("emanuel-campos88@acaoi.com.br")
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("CFIMA5qmR6")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("09169-206")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_btnAddressFind").click()
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("444")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("66989932400")
    time.sleep(5) 
    context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
    

@when(u'I inform the email {email} and the password {password}')
def step_impl(context, email, password):
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(email)
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys(password)
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()

@when(u'I choose the banner and the product')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.swiper-pagination-bullet:nth-child(2)").click()
    context.driver.find_element(By.CSS_SELECTOR, ".div.swiper-slide:nth-child(3) > a:nth-child(1) > picture:nth-child(1) > img:nth-child(3)").click()
    context.driver.find_element(By.CSS_SELECTOR,'.li.item[data-idproductline="141"] > div.product-item > a[data-idproduct="31138"]').click()

@when(u'I inform zip code and date of delivery')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_uwcCalendar_txtZip").send_keys('09169')
    context.driver.find_element(By.ID, "ContentSite_uwcCalendar_txtZipComplement").send_keys('206')
    context.driver.find_element(By.CSS_SELECTOR, ".btn_okcep.jSelectZip").click()
    context.driver.find_element(By.CSS_SELECTOR, ".data_dia > li:nth-child(31) > span:nth-child(1) > a:nth-child(1)").click()
    context.driver.find_element(By.CSS_SELECTOR, ".box_periodos > ul:nth-child(3) > li:nth-child(1) > input:nth-child(1)").click()
    context.driver.find_element(By.ID, "btConfirmShippingData").click()


@when(u'I include the product in the cart')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()


@then(u'I check the name and price')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".prodBasket_nome > a:nth-child(1)").text == "Mini Orquídea Rara Amarela"
    assert context.driver.find_element(By.CSS_SELECTOR, ".precoPor_basket").text == "R$ 99,90"

    context.driver.quit()
    
@then(u'I will be successfully directed to a Home page')
def step_impl(context):
    nome_boas_vindas = "Emanuel"
    time.sleep(5)
    context.driver.find_element(By.ID, "perfil-hidden").click()
    assert context.driver.find_element(By.CSS_SELECTOR, ".meuperfil").text == f'Boa Noite, {nome_boas_vindas}!' 
    context.driver.quit()
    
@then(u'shows the login ATENÇÃO - e-mail ou senha inválidos! error')
def step_impl(context):
    time.sleep(5)
    error_message = "ATENÇÃO - e-mail ou senha inválidos!"
    assert context.driver.find_element(By.CSS_SELECTOR, ".aviso-erro").text == error_message

    context.driver.quit()
    


