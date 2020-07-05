from src.dfGenator import *
import time 

empresaShow = []
brk = 1
while brk != 2:
    empresa = input('Digite o nome da empresa, para prossegirmos: ')
    lenEmp = int(input('Quantos links irá entrar para buscar informações: '))
    brk = int(input('Se quiser outra empresa digite [1] se não digite [2]: '))
    empresaShow.append(empresa)
    empresaShow.append(lenEmp)
    



links_gerados = GeradorDeLinks(empresaShow)
for links in links_gerados:
    print("O links gerado foi: ", links)

    
for data in VarredorDePaginas(links_gerados):
    print(data)
    
