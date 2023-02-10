from api.dropbox import upload_file_to_dropbox
from api.google_drive import upload_file_to_google_drive
from api.onedrive import upload_file_to_one_drive

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # upload_file_to_google_drive("building.jpg")
    print(upload_file_to_dropbox('building.jpg'))

