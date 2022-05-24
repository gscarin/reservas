from logging import exception
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from users import EMAIL,PASS,RECIEVER
import yagmail


while True:
    try:
        options = webdriver.ChromeOptions()
        ##options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.set_window_size(595, 900)


        driver.get('https://acasadoporco.com.br/')
        time.sleep(10)

        driver.find_element_by_xpath('//*[@id="header"]//div//div//div//div[2]//div//a').click()

        #reserva
        driver.find_element_by_xpath('//*[@id="menu-item-14846"]//a//span//span').click()
        time.sleep(2)

        ##acha o botao
        driver.find_element_by_xpath('//modal-container//div//div//div//ul//li//a').click()
        time.sleep(5)

        ## acha o form
        driver.find_element_by_xpath("//form//div//div//div//div//div").click()

        time.sleep(2)

        lista = driver.find_elements_by_xpath("//form//div//div//div//ul//li")
        time.sleep(1)

        ## driver.close()

        for i in lista:
            if i.text == '24 maio 2022 (terça-feira)':
                yagmail.SMTP(EMAIL,PASS).send(RECIEVER, 'Reserva para o aniversario da carol')
                
            else:
                print("Fechou e nao achou, esperando 5 min para comecar de novo")
        driver.quit()

    except (WebDriverException, TimeoutException):
        print("Go to while loop from the begining")
        continue

           

