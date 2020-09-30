
#Import function connect to Google Drive
from connection_drive import *
# Import for arguments
import sys
from googleapiclient.http import MediaFileUpload

def fn_upload(filename):
    # Folder where upload files
    folder_id="1F81IxqDbE1TKxNeYP9P9SYrWWoBk5BSr"
    body = {'name': filename, 'mimeType': 'application/zip',"parents":[folder_id]}
    media = MediaFileUpload(filename, mimetype='application/zip')
    fiahl = result[1].files().create(body=body, media_body=media).execute()
    print('Upload File: %s' % filename)


# Start process
if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = connect()
        items=result[0]
        filename = sys.argv[1]
        fn_upload(filename)
        
    else:
        print("Please, need argument")