from src.caminho import start
from src.start import Bot
from src.caminho import nav
from bs4 import BeautifulSoup as bs
from time import sleep as slp

#gera os links com a formatação pra mandar o selenium varrer pagina por página
def GeradorDeLinks(array):
    dataLinks = []
    #gravando os links que vão ser atribuido na procura no dataLinks já com a formatação
    for emp, qnt in zip(array[::2], array[1::2]):
        print(emp, qnt)
        for link in start(emp, qnt):
            dataLinks.append(f'https://www.reclameaqui.com.br{link}')

    
    return dataLinks




#esse varredor ira procurar os links de comentários individuais de cada empresa
def VarredorDePaginas(links):
    for link in links:
        #navegando nos links das empresas selecionadas por você
        nav().get(link)
        slp(2)

        nav().find_element_by_xpath('//*[@id="menu"]/ul/li[2]/a')
        slp(3)

        data = []
        dados_pag = nav().page_source
        data = pag_web = bs(dados_pag, 'html.parser')
        return data 


      





