#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Importa bibliotecas
try:
    print('\n\nImportando bibliotecas...')
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import argparse
    print('\nIniciando a aplicacao...')
except Exception as E:
    exit(print(E))



#Declara variaveis
parser = argparse.ArgumentParser()
parser.add_argument('-a', required=True)
textoAPesquisar = vars(parser.parse_args())
textoAPesquisar = textoAPesquisar["a"]

url = 'http://localhost/php-python/4button.php'
caixaDePesquisaName = 'name'
botaoPesquisarName = 'botao'
print('\nVariaveis declaradas.')



#Abre navegador
try:
    navegador = webdriver.Chrome()
    print('\nNavegador aberto.')
except Exception as E:
	exit(print(E))


#Acessa pagina
try:
    navegador.get(url)
    print('\nPagina carregada.')
except Exception as E:
    exit(print(E))


#Busca elemento Caixa de pesquisa -> Limpa conteudo -> Insere valor  
try:
    caixaDePesquisa = navegador.find_element_by_name(caixaDePesquisaName)
    caixaDePesquisa.clear()
    caixaDePesquisa.send_keys(str(textoAPesquisar))
    print('\nValor inserido.')
except Exception as E:
    exit(print(E))


#Busca elemento Botao de pesquisa -> Executa click  
try:
    botaoPesquisar = navegador.find_element_by_name(botaoPesquisarName).click()
    print('\nBotao clicado.')
except Exception as E:
    exit(print(E))


#assert "No results found." not in driver.page_source

print('\nFinalizando a aplicacao...\n')
navegador.close()
