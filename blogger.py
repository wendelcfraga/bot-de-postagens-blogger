#!/usr/bin/env python
#-*- coding: utf-8 -*-

__autor__ = "Wendel Fraga"
__email__ = "costa.wendel@ufg.br"
__status__ = "POC"

# Git: @wendelfraga

from bs4 import BeautifulSoup as bs
import requests 
import wikipedia
import time
import sys
from oauth2client import client
from googleapiclient import sample_tools
from postagem import *
import os
import json



def main(argv):
	service, flags = sample_tools.init(
      argv, 'blogger', 'v3', __doc__, __file__,
      scope='https://www.googleapis.com/auth/blogger')

	with open('keys.json') as key:
		keys = json.load(key)

	try:
		termoASerBuscado = input(str("[+] Nome do game que desejar: "))
		paginaHtml = u"https://1337x.to/category-search/{}/Games/1/".format(termoASerBuscado)
		requisicaoSite = requests.get(paginaHtml)
		bsObjeto = bs(requisicaoSite.text, 'lxml')
		listaDeItens = bsObjeto.find_all("td", {"class": "coll-1 name"})

		listaPostagem = []

		for nome in listaDeItens:
			for a in nome.find_all("a", href=True):
				dadosPostagem = {}
				user = a.next.findNext("a", href=True)
				user = user['href']
				link = a['href']

			dadosPostagem['nome'] = nome.get_text()	
			dadosPostagem['user'] = user.split('/')[2]
			dadosPostagem['link'] = u"{}{}".format("https://1337x.to",link)

			listaPostagem.append(dadosPostagem)	

            
		for item in listaPostagem:
			paginaDoLink = item['link']
			requisicaoPaginaDoLink = requests.get(paginaDoLink)
			paginaSoup = bs(requisicaoPaginaDoLink.text, 'lxml')
			urlDeDownload = paginaSoup.find("ul", {"class": "dropdown-menu"})
			linkDeDownload = urlDeDownload.find("a", href=True)
			
			print("\n\n")
			print("[+] Usuário: ", item['user'], "[+] Nome do jogo: ", item['nome'],\
			 "[+] Link: ", linkDeDownload['href'])	
			print("\n\n")

			blogs = service.posts()
			wikipedia.set_lang("pt")
			descricaoDaPostagem = wikipedia.summary(termoASerBuscado, sentences=5)
			nomeDaPostagem = item['nome']
			nomeDoResponsavelP = item['user']

			print("[+] Nome da postagem que será feita: " + nomeDaPostagem)
			print("\n\n")

			definirPostagem(nomeDoPost=nomeDaPostagem, descricaoDoPost=descricaoDaPostagem, linkDoBlog=linkDeDownload['href'], nomeDaImagem=termoASerBuscado, responsavelPost=nomeDoResponsavelP)

			fazerPostagem = blogs.insert(blogId=keys['bloggerID'], body=bodyDapostagem).execute()

			print("[+] Postagem: ", fazerPostagem)
			print("\n\n")
			print("==================================================")
			print("\n\n")
			print("[+] Url do post: ", fazerPostagem['url'])
			print("\n\n")
			print("==================================================")

			time.sleep(20)

	except client.AccessTokenRefreshError:
		print ('[-] Erro de autenticação -> verifique o seu Token!')	

	except requests.exceptions.ConnectionError:
		print('[-] Erro ao tentar acessar Wikipédia!')

	except wikipedia.exceptions.PageError:
		print("[-] Não existe essa página na Wikipédia!")
				

	except IndexError as e:
		print("[-] Erro encontrado em lista!", e)
		print("\n\n")
		print("[-] Programa encerrado!")
		print("[*] Limpando arquivos.....")
		time.sleep(3)
		os.remove("imagem/imgurl.txt")	
		os.remove("video/vidurl.txt")
		
	except NameError as e:
		print(" [-] Erro encontrado em alguma variável!", e)
		print("\n\n")
		print("[-] Programa encerrado!")
		print("[*] Limpando arquivos.....")
		time.sleep(3)
		os.remove("imagem/imgurl.txt")	
		os.remove("video/vidurl.txt")

	except KeyboardInterrupt:
		print("\n\n")
		print("[-] Programa encerrado!")
		print("[*] Limpando arquivos.....")
		time.sleep(3)
		try:
			os.remove("imagem/imgurl.txt")	
			os.remove("video/vidurl.txt")

		except FileNotFoundError:
			print("\n\n")
			print("[*] Sem arquivos para limpar!")	
				

					
if '__main__' == __name__:
	main(sys.argv)
