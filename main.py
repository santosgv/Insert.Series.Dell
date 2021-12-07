import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import time
#import random

class Raspagem:
    def __init__(self):
        options = Options()
        #options.headless=True
        options.add_argument("--disable-notifications")
        path="C:/Users/vitorgomes/PycharmProjects/dellseries/chromedriver.exe"
        self.driver = webdriver.Chrome(path,chrome_options=options)
        driver = self.driver
        driver.get("https://support.hp.com/br-pt/add-device")

        # Botao de logar
        WebDriverWait (self.driver.find_element(By.CSS_SELECTOR, '#SignIn').click(),50)
        time.sleep(30)
        # input de login
        WebDriverWait(self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('inventario.ti@patrus.com.br', Keys.ENTER),10)
        time.sleep(30)
        # input de senha
        WebDriverWait(self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('Tipatrus21@', Keys.ENTER),10)
        time.sleep(30)
        self.Series()

    def Series(self):
        quantidade=0
        erro=0
        # abre o arquivo de series
        Arquivo = open("series.txt")
        Series = Arquivo.readlines()
        # lop de insersao das series do arquivo
        for numero_serie in Series:
            try:
                WebDriverWait(self.driver.get('https://support.hp.com/br-pt/add-device'),10)
                time.sleep(3.5)
                WebDriverWait(self.driver.find_element(By.XPATH,
                                                       '//*[@id="directionTracker"]/app-layout/app-add-device/div[1]/app-product-finder/div/div/div/div/div[1]/div[2]/div/app-general-add-device/app-device-add-box/div/div[1]/div[1]/div/input').send_keys(
                    numero_serie, Keys.ENTER), 10)

                WebDriverWait(self.driver.get('https://support.hp.com/br-pt/add-device'),10)
                quantidade=quantidade + 1
                print(f'quantidade que inseriu {quantidade}')

            except Exception :
                with open('Garantias.txt', 'a') as arquivo:
                    arquivo.write(f'\n{numero_serie}')
                    arquivo.close()
                    erro = erro + 1
                    print(f" quantidade de erro {erro}")
            finally:
                pass




bot=Raspagem()

