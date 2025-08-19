from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def run_backup():
    try:
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()  # Opens browser first time only
        drive = GoogleDrive(gauth)

        # Check if SoulRoomBackup exists
        folder_list = drive.ListFile({'q': "title='SoulRoomBackup' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
        if folder_list:
            folder_id = folder_list[0]['id']
        else:
            folder_metadata = {'title': 'SoulRoomBackup', 'mimeType': 'application/vnd.google-apps.folder'}
            folder = drive.CreateFile(folder_metadata)
            folder.Upload()
            folder_id = folder['id']

        # Upload everything fresh from templates and static
        for root, dirs, files in os.walk('.'):
            if 'templates' in root or 'static' in root:
                for file in files:
                    file_path = os.path.join(root, file)
                    f = drive.CreateFile({'title': file, 'parents': [{'id': folder_id}]})
                    f.SetContentFile(file_path)
                    f.Upload()

        print("☁️ Backup complete to SoulRoomBackup")

    except Exception as e:
        print("⚠️ Backup failed:", e)
