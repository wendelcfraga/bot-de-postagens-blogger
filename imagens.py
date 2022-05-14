#-*- coding: utf-8 -*-
from google_images_search import GoogleImagesSearch
import json

#Cria arquivo para salvar as urls das imagens
def pesquisarImg(termo):
	with open('keys.json') as key:
		keys = json.load(key)

	arquivoImgUrl = open("imagem/imgurl.txt", "w")
	gis = GoogleImagesSearch(str(keys['googleCustomSearchAPI']), str(keys['googleCustomSearchID']))
	
	_search_params = {
		'q': str(termo),
		'num': 10,
		'fileType': 'jpg|png',
	}

	gis.search(search_params=_search_params)
	for image in gis.results():
		arquivoImgUrl.writelines(image.url + '\n')
		#print(image.referrer_url)

	arquivoImgUrl.close()

		





