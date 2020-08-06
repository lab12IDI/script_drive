
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
            if item['name']==str(sys.argv[1]):
                print(u'{0} ({1})'.format(item['name'], item['id']))
                download(item['id'],service,item['name'])
                break
    else:
        print("Please, need argument")