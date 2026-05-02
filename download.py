import os
import shutil


file_types = {
    "Video": [".mp4", ".mkv", ".mpg", ".3gp"],
    "Music": [".mp3", ".wav", ".m4a"],
    "Software": [".deb", ".exe", ".apk"],
    "Photos": [".png", ".jpg", ".jpeg", ".gif", ".webm", ".bmp"],
    "Disk_Image": [".iso"],
    "Document": [".pdf", ".docx", ".doc", ".odt", ".mhtml", ".html"],
    "Contacts": [".vcf"],
    "Compressed_Files": [".zip",".xz",]
}

download_path = "/home/debojit26/Downloads"

def organize_files():
    for filename in os.listdir(download_path):
        print(f"চেক করছি: {filename}")
        filepath = os.path.join(download_path, filename)

        if os.path.isfile(filepath):
            extension = os.path.splitext(filename)[1].lower()

            for folder, extensions in file_types.items():

                if extension in extensions:

                    target_folder = os.path.join(download_path, folder)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    shutil.move(filepath, os.path.join(target_folder, filename))
                    break 
organize_files()
