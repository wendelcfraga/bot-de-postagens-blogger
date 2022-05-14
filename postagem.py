#-*- coding: utf-8 -*-

# Autor: @wendelfraga
# Email: costa.wendel@ufg.br

import random
import time
import requests 
from bs4 import BeautifulSoup as bss
from imagens import *
from videos import *
import json

with open('keys.json') as key:
		keys = json.load(key)

bodyDapostagem = {
        "kind": "blogger#post",
        "title": "",
        "labels" : [""],
        "content": """
"""
        }


def definirPostagem(nomeDoPost, descricaoDoPost, linkDoBlog, nomeDaImagem, responsavelPost):
	googleImagem = nomeDaImagem + " screenshots" #Coloque aqui a categoria de imagens que deseja buscar

	pesquisarImg(googleImagem)

	with open("imagem/imgurl.txt", "r") as arquivoImg:
	    conteudoGImages = arquivoImg.readlines()
	arquivoImg.close()

	urlsGoogleImg = []

	for linkImg in conteudoGImages:
	    urlsGoogleImg.append(str(linkImg).replace('\n', "")) 

	print("[+] imagens do Google: ", urlsGoogleImg)
	print("\n\n")

	pegarVideos(nomeDaImagem + " gameplay") #Coloque a categoria de vídeos que deseja buscar

	arquivoLinkDeVideos = open("video/vidurl.txt", "r")
	
	listaDeVideosBing = []
	for line in arquivoLinkDeVideos.readlines():
		listaDeVideosBing.append(line)
		time.sleep(2)
	arquivoLinkDeVideos.close()		

	
	#Edite esse HTML para ficar de acordo com o padrão de postagem do seu Blog.		
	corpoDaPostagem = """
			<div>
			<img src="{}">
			</div>
			<br>
			<div>
			<p>Descrição: {}</p>
			</div>
			<br>
			<img src="{}">
			<img src="{}">
			<img src="{}">
			<br>
			<iframe width="720" height="405" src="{}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
			<br>
			<br>
			<a href="{}">Link de Download</a>
			<br>
			<p>Responsável pela postagem: {}</p>

	""".format(random.choice(urlsGoogleImg), descricaoDoPost,\
	random.choice(urlsGoogleImg), random.choice(urlsGoogleImg), random.choice(urlsGoogleImg),\
	random.choice(listaDeVideosBing), linkDoBlog, responsavelPost)

	
	palavrasChave = nomeDaImagem #Coloque a categoria de palavras chave que você deseja inserir na postagem.	
	chaves = {"seeds": palavrasChave, "engine": "google", "country": "BR", "type": "broad"}
	requisicaoChaves = requests.get('https://api.lc.wordtracker.com/v2/search?&app_id=97ff30c3&app_key={}'.format(str(keys['chaveApiWordTracker'])), params=chaves)
	textoJson = json.loads(requisicaoChaves.text)

	listaDePalavrasChave = []

	for resultado in textoJson['results']:
		listaDePalavrasChave.append(resultado['keyword'])

	for item in listaDePalavrasChave:
		print(item)
	
	bodyDapostagem['title'] = nomeDoPost
	bodyDapostagem['labels'] = listaDePalavrasChave
	bodyDapostagem['content'] = corpoDaPostagem

	print(bodyDapostagem)

	#definirPostagem("Exemplo de nome da postagem", "Exemplo descrição.", "exemplolink.com", "exemplo tag alt", "exemplo responsável pelo post")	
	