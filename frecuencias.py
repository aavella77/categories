""" Programa de frecuencia de categorias """
import os, glob, operator, csv

def init_resultado():
	resultado = {}
	with open("categorias.txt", "r") as categorias:
		for categoria in categorias:
			categoria = categoria.strip()
			resultado[categoria] = 0
	return resultado		

resultado = init_resultado()
for file in os.scandir("input"):
	output_file = os.path.join("output", file)
	output_file = output_file.replace(".txt", "_resultado.csv")
	output_file = output_file.replace("input/", "")
	with open(file, "r") as fin:	
		for categoria in resultado.keys():
			fin.seek(0)
			for linea in fin:
				if categoria.lower() in linea.lower():
					resultado[categoria] += 1 		
		with open(output_file, 'w') as fout:
		  fout.write('{}, {}\n'.format("Categoria", "Num"))	
		  for k,v in sorted(resultado.items(), key=lambda x:x[1], reverse=True):
		    fout.write('{},{}\n'.format(k, v))
		resultado = init_resultado()    		
		