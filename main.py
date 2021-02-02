#!/bin/python3

#Import function connect to Google Drive
from connection_drive import *

#Impot tools 
from functions import *

#Import module for arguments
import sys


def main():

	# Coger la conexion al Drive
	result = connect()

	# Carpetas del Drive
	foldersNGS=result[0]

	# Conexion del Drive
	service=result[1]

	   

	if sys.argv[1] == "--dSamples":
		
		f = open("samples.txt")
		linea = f.readline()

		while linea != "":

		  print("Compienza la búsqueda de la muestra: "+linea)
		  
		  # Búsqueda de la muestra en Drive
		  downloadSample(linea,foldersNGS,service)

		  linea = f.readline()
		
		f.close()


	elif sys.argv[1] == "--dId":

		print("Descargar fichero con su ID")

	elif sys.argv[1] == "--searchId":

		print("Extraer los ID")

		print(foldersNGS)

	elif sys.argv[1] == "--dSelectFolders":

		contSamples = 0
		folders = ["1ZgrmxqdU9ZaO3HvoVfn5UnrKHipkBkI0","10K5oL394vnnNuCJQSQpIb7OQuL5Dn7KU","1rnjfAT43rFOOU5FRob-Ct2CSLTOEk2jb"]

		for item in folders:
			# Accedemos a los items de la raiz
			query="'"+item+"' in parents"
			results = service.files().list(q=query, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
			subitems = results.get('files', [])
			searchAllFiles(subitems,result,service,contSamples)

		print("Numero de muestas descargadas : "+str(contSamples))

	elif sys.argv[1] == "--viewIDs":

		for i in foldersNGS:
			print(i['id']+"      "+i['name'])

	else:

		print("Debes especificar un comando, para más información consulta el README")




if __name__ == '__main__':
	main()