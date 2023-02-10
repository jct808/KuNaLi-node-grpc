import pathlib
import pandas as pd
import dropbox
from dropbox.exceptions import AuthError

# ay1kisDmEhsAAAAAAAABJvqHXunA-k8G779aN5iPvLQ


DROPBOX_ACCESS_TOKEN = 'sl.BYiihe23NAUZGz1fDjXzDN_3w9R20XtrwCpOO_yXwtWHx8LHN2nAHJ5MqEdW_6iZPdHkR4299yRPbv6fvbClCqtYgcxXpEHHDTNInIoJOK8wMSQ9DYyEWXC6OWG2ImOcJPfZK60BAbFq'


def dropbox_connect():
    """Create a connection to Dropbox."""
    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))
    return dbx


def dropbox_list_files(path):
    """Return a Pandas dataframe of files in a given Dropbox folder path in the Apps directory.
    """

    dbx = dropbox_connect()

    try:
        files = dbx.files_list_folder(path).entries
        files_list = []
        for file in files:
            if isinstance(file, dropbox.files.FileMetadata):
                metadata = {
                    'name': file.name,
                    'path_display': file.path_display,
                    'client_modified': file.client_modified,
                    'server_modified': file.server_modified
                }
                files_list.append(metadata)

        df = pd.DataFrame.from_records(files_list)
        return df.sort_values(by='server_modified', ascending=False)

    except Exception as e:
        print('Error getting list of files from Dropbox: ' + str(e))


def upload_file_to_dropbox(file_name):
    """Upload a file from the local machine to a path in the Dropbox app directory.

    Args:
        local_path (str): The path to the local file.
        local_file (str): The name of the local file.
        dropbox_file_path (str): The path to the file in the Dropbox app directory.

    Example:
        dropbox_upload_file('.', 'test.csv', '/stuff/test.csv')

    Returns:
        meta: The Dropbox file metadata.
    """
    local_path = '.'

    try:
        dbx = dropbox_connect()

        local_file_path = pathlib.Path(local_path) / file_name

        with local_file_path.open("rb") as f:
            meta = dbx.files_upload(f.read(), f"/{file_name}", mode=dropbox.files.WriteMode("overwrite"))

            return meta
    except Exception as e:
        print('Error uploading file to Dropbox: ' + str(e))