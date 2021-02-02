
#Import function connect to Google Drive
from connection_drive import *

# Import for arguments
import sys




# Function to Download
def download(idFile,service,filename):
    request = service.files().get_media(fileId=idFile)
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


def searchAllFiles(subitems,result,service,contSamples):
	#Buscamos dentro de las carpetas que se encuentran
	for sample_name in subitems:

		#Accedemos a la carpeta de la muestra
		ult_query="'"+sample_name['id']+"' in parents"
		ult_result = service.files().list(q=ult_query, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
		sample = ult_result.get('files', [])

		#Recorremos los ficheros de la carpeta
		for s in sample:

			#Accedemos a la carpeta de Analisis de la muestra
			ult_q="'"+s['id']+"' in parents"
			ult_r = service.files().list(q=ult_q, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
			returnExcel = ult_r.get('files', [])

			#Recorremos los ficheros de la carpeta de Analisis
			for i in returnExcel:
				if i['name'] == sample_name['name']+".xlsx":
					print(i['name'])
					contSamples = contSamples+1
					download(i['id'],service,i['name'])
					break

				#download(i[0],service,i['name'])
                

def searchFilesFilter(subitems,result,service,sample):
	#Buscamos dentro de las carpetas que se encuentran
	for i in subitems:
	    # Si encontramos la muestra
	    if i['name']==str(sample):
	        print("Muestra encontrada ..... "+sample)

	        #Accedemos a la carpeta de la muestra
	        ult_query="'"+i['id']+"' in parents"
	        ult_result = service.files().list(q=ult_query, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
	        sample = ult_result.get('files', [])

	        #Recorremos los ficheros de la carpeta
	        for s in sample:
	            #Accedemos a la carpeta de Analisis de la muestra
	            if s['name'] == "Analisis_"+sample:
	                
	                ult_q="'"+s['id']+"' in parents"
	                ult_r = service.files().list(q=ult_q, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
	                returnExcel = ult_r.get('files', [])

	                #Recorremos los ficheros de la carpeta de Analisis
	                for i in returnExcel:
	                    #Si encontramos el fichero de analisis lo descargamos

	                    if i['name']==sample+".xlsx":
	                        #download(i['id'],service,i['name'])
	                        print(i['name']==sample+".xlsx")
	                        brea


def downloadSample(sample,folderNGS,service):

	for folder in folderNGS:

		query="'"+folder['id']+"' in parents"
		results = service.files().list(q=query, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
		subitems = results.get('files', [])

		#Buscamos dentro de las carpetas que se encuentran
		for i in subitems:
			# Si encontramos la muestra
			if i['name']==str(sample):
			    print("Muestra encontrada ..... "+sample)
			    #Accedemos a la carpeta de la muestra
			    ult_query="'"+i['id']+"' in parents"
			    ult_result = service.files().list(q=ult_query, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
			    sample = ult_result.get('files', [])
			    #Recorremos los ficheros de la carpeta
			    for s in sample:
			    	#Accedemos a la carpeta de Analisis de la muestra
			    	if s['name'] == "Analisis_"+i['name']:
			    		ult_q="'"+s['id']+"' in parents"
			    		ult_r = service.files().list(q=ult_q, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
			    		returnExcel = ult_r.get('files', [])
			    		#Recorremos los ficheros de la carpeta de Analisis
			    		for it in returnExcel:
			    			#Si encontramos el fichero de analisis lo descargamos
			    			if it['name']==i['name']+".xlsx":
			    				download(it['id'],service,it['name'])
			    				break



