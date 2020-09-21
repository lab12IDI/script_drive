
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


# Start process
if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = connect()
        items=result[0]
        service=result[1]
        for item in items:
            # Accedemos a los items de la raiz
            query="'"+item['id']+"' in parents"
            results = service.files().list(q=query, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
            subitems = results.get('files', [])

            #Buscamos dentro de las carpetas que se encuentran en NGS
            for i in subitems:
                # Si encontramos la muestra
                if i['name']==str(sys.argv[1]):
                    print("Muestra encontrada ..... "+sys.argv[1])

                    #Accedemos a la carpeta de la muestra
                    ult_query="'"+i['id']+"' in parents"
                    ult_result = service.files().list(q=ult_query, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
                    sample = ult_result.get('files', [])

                    #Recorremos los ficheros de la carpeta
                    for s in sample:
                        #Accedemos a la carpeta de Analisis de la muestra
                        if s['name'] == "Analisis_"+sys.argv[1]:
                            
                            ult_q="'"+s['id']+"' in parents"
                            ult_r = service.files().list(q=ult_q, spaces='drive',fields="nextPageToken, files(id, name,parents)").execute()
                            returnExcel = ult_r.get('files', [])

                            #Recorremos los ficheros de la carpeta de Analisis
                            for i in returnExcel:
                                #Si encontramos el fichero de analisis lo descargamos

                                if i['name']==sys.argv[1]+".xlsx":
                                    download(i['id'],service,i['name'])
                                    break            
    else:
        print("Please, need argument")