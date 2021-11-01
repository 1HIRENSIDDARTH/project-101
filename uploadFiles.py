import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.aT = access_token

    def upload_file(self, file_from):
        db = dropbox.Dropbox(self.aT)
        fileName = os.path.split(
            file_from)[1]

        dropbox_file = '/CloudStorage/'+fileName

        with open(file_from, "rb") as f:
            db.files_upload(f.read(), dropbox_file,
                            mode=dropbox.files.WriteMode.overwrite)


AccessToken = "uzBbV9lW0HMAAAAAAAAAAfCXnd0beUFqwV4tu3ce-svjhzZ4QSv_nEHE8pMhVwS6"

cloudStoring = TransferData(AccessToken)

fileFrom = input("Enter File Path To Transfer ")

while(os.path.isfile(fileFrom) == False):
    print("Pls Give The Path Of A File")
    fileFrom = input("Enter File Path To Transfer ")

cloudStoring.upload_file(fileFrom)

print("Files Have Been Moved")