""" Programa de frecuencia de categorias """
import os

NUMBER_OF_CATEGORIES = 30

def init_resultado():
	resultado = {}
	with open("categorias.txt", "r") as categorias:
		for categoria in categorias:
			categoria = categoria.strip()
			resultado[categoria] = 0
	return resultado		

resultado_global = {}
resultado_global_peso = {}
with open("categorias.txt", "r") as categorias:
	for categoria in categorias:
		categoria = categoria.strip()
		resultado_global[categoria] = 0
		resultado_global_peso[categoria] = 0	

resultado = init_resultado()
for file in os.scandir("input"):
	output_file = os.path.join("output", file)
	output_file = output_file.replace(".txt", "_resultado.csv")
	output_file = output_file.replace("input/", "")
	big_string = ""
	fin = open(file, "r")
	lineas = fin.readlines()
	for linea in lineas:
		big_string = big_string + linea.strip() 	
	for categoria in resultado.keys():
		resultado[categoria] = big_string.count(categoria.lower())
		resultado_global[categoria] += resultado[categoria]
	with open(output_file, 'w') as fout:
	  fout.write('{}, {}\n'.format("Categoria", "Num"))	
	  for k,v in sorted(resultado.items(), key=lambda x:x[1], reverse=True):
	    fout.write('{},{}\n'.format(k, v))
	resultado = init_resultado() 

with open("archivo_resumen.csv", "w") as fout3:
	for file in os.scandir("output"):
		fout2 = open(file, "r")
		title = str(file) + ",num,"
		title = title.replace("'","")
		title = title.replace("<","")
		title = title.replace(">","")				
		title = title.replace("DirEntry","")
		fout3.write(title)
	fout3.write("\n")
	for idx in range(NUMBER_OF_CATEGORIES):
		for file in os.scandir("output"):
			fout4 = open(file, "r")
			for _ in range(idx+2):
				cat_num = fout4.readline().strip() + ","
			for categoria in resultado.keys():
				if int(cat_num.split(",")[1]) > 0:
					resultado_global_peso[categoria] += cat_num.count(categoria)				
			fout3.write(cat_num)	
		fout3.write("\n")		

idx = 0
with open("archivo_analisis.csv", 'w') as fout5:
	fout5.write('{}, {}, {}\n'.format("Categoria", "Num", "Peso"))	
	for key,value in sorted(resultado_global.items(), key=lambda x:x[1], reverse=True):
		if idx < NUMBER_OF_CATEGORIES:
			fout5.write('{},{},{}\n'.format(key, value, resultado_global_peso[key]))
		idx += 1	

