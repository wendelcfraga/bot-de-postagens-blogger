#-*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup as bs
import time

#Pega embed de vídeos do Youtube no resultado do bing para anexar a postagem.
def pegarVideos(termoASerBuscado):
	pesquisa = "https://www.bing.com/videos/search?q=" + termoASerBuscado
	requisicaoYoutube = requests.get(pesquisa)
	htmlYoutube = bs(requisicaoYoutube.text, "lxml")	
	urlsYoutube = htmlYoutube.find_all("a")
	listaYoutube = []

	for link in urlsYoutube:
		try:
			if "https://www.youtube.com" in link["href"]:
				listaYoutube.append(link["href"].replace("https://www.youtube.com/watch?v=", "https://www.youtube.com/embed/"))
		except KeyError:
			pass

	for item in listaYoutube:
		if "user" or "channel" in item:
			listaYoutube.remove(item)
					
	with open("video/vidurl.txt", "w") as arquivoUrlVideos:
		for item in listaYoutube:
			arquivoUrlVideos.write("%s\n" % item)
			time.sleep(2)

	arquivoUrlVideos.close()
