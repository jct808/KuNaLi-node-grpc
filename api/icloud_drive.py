from pyicloud import PyiCloudService
from datetime import datetime


def upload_file_to_icloud(file_name):
    try:
        api = PyiCloudService('jct808@gmail.com')
        with open(file_name, 'rb') as file_in:
            api.drive['Desktop'].upload(file_in)    # Upload file to iCloud
            today = datetime.now()    # Month abbreviation, day, year and time
            current_datetime = today.strftime("%b-%d-%Y-%H-%M-%S")
            api.drive['Desktop']['building.jpg'].rename(f'{current_datetime}.jpg')  # Rename
    except FileNotFoundError:
        print("Upload file not exist!")
    except ConnectionError:
        print("Connect Error!")


if __name__ == '__main__':
    upload_file_to_icloud("building.jpg")
