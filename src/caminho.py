from src.start import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as slp
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs


driver = webdriver.Chrome()
url = 'https://www.reclameaqui.com.br/'
bot = Bot(driver, url)
bot.navigate()

def nav():
    return bot.startBot()
    

def InterandoEmpresas(name):
    input_empresa = nav().find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div/div/div/div/input')
    input_empresa.clear()
    input_empresa.send_keys(name)
    slp(5)
       
def GerandoLinks(quant):
    # Transformando os dados da pag em um dados bs4
    dados_pag = nav().page_source
    dados_pag_bs4 = bs(dados_pag, 'html.parser')
    #obtendo os links para interar no reclame aqui
    links_interators = [x.get('href') for x in dados_pag_bs4.find_all('a', 'vueperslide')]
    return links_interators[:quant]

   
   
def start(names, quants):
    InterandoEmpresas(names)
    data = GerandoLinks(quants)
    return data
    

            

    
