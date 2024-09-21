import os
from pathlib import Path

class Attachment():
    def __init__(self, filename, filebytes, downloads_folder = 'downloads', keep_files = True):
        self.name = filename
        self.filebytes = filebytes
        self.type = filename.split('.')[-1].upper()
        self.downloads_folder = downloads_folder
        self.path = self.check_safe_path()
        self.keep_files = keep_files

    def check_safe_path(self):
        if Path(self.downloads_folder).exists() is False:
            Path(self.downloads_folder).mkdir()

        if Path(f'{self.downloads_folder}/{self.name}').exists():
            self.name = f'{Path(self.name).stem}_copy{Path(self.name).suffix}' #This need to be improved in helpers.formatters!

        relative_path = f'{self.downloads_folder}/{self.name}'

        return Path(relative_path).resolve()

    def save_file(self):
        with open(self.path, 'wb') as file:
            file.write(self.filebytes)
        print(f'\n[+] Saved file: {self.name}')

    def delete_file(self):
        if Path(self.path).exists() and self.keep_files is False:
            os.remove(self.path)