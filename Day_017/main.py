from os import makedirs, path
from getpass import getpass
import rarfile
from zipfile import ZipFile
from py7zr import SevenZipFile
from pyzipper import AESZipFile, ZIP_DEFLATED, WZ_AES

# file = "/home/pnk/Downloads/Animate.zip"
# file = "/home/pnk/Downloads/wallpaper.zip"
# file_path = "/home/pnk/Downloads/wallpaper.rar"
# file_path = "/home/pnk/Downloads/Animate.7z"
file_path = "/home/pnk/Downloads/Animate_storyboard_sequence_to_v…_202607251610.mp4"
extract_path = "/home/pnk/Downloads/"


def extract_zip(file_path, extract_path):

    makedirs(extract_path, exist_ok=True)

    with ZipFile(file_path, "r") as zf:
        try:
            zf.extractall(path=extract_path)
            print("success!")
        except RuntimeError as e:

            if "password required" in str(e):

                while True:

                    pwd = getpass("Enter Password: ")

                    try:
                        zf.extractall(path=extract_path, pwd=pwd.encode("utf-8"))
                        print("success!")
                        break

                    except RuntimeError as e:

                        if "bad password" in str(e).lower():
                            print("Wrong Password , Try again")

            else:
                print("Extraction Failed")


def extract_7z(file_path, extract_path):
    makedirs(extract_path, exist_ok=True)

    with SevenZipFile(file_path, "r") as sz:
        if sz.needs_password():
            while True:

                pwd = getpass("Enter Password: ")

                try:
                    with SevenZipFile(file_path, "r", password=pwd) as sz:
                        sz.extractall(path=extract_path)
                        print("success!")
                        break

                except Exception as e:
                    print(e)

        else:
            sz.extractall(extract_path)
            print("success!")


def create_zip(source, output_filename: str, password: bool = False):
    files = source
    if not files:
        print("Error: No files to archive")
        return

    try:
        if password:
            with AESZipFile(
                output_filename, "w", compression=ZIP_DEFLATED, encryption=WZ_AES
            ) as zf:
                pwd = getpass("Enter Password: ")
                zf.setpassword(pwd.encode("utf-8"))
                zf.write(files, path.basename(files))
        else:
            with AESZipFile(output_filename, "w", compression=ZIP_DEFLATED) as zf:
                zf.write(files, path.basename(files))
    except:
        print("Error:")


def create_7z(source, output_filename, password: str | None = None):
    files = source
    if not files:
        print("Error: No files to archive")
        return

    try:
        with SevenZipFile(output_filename, "w", password=password) as sz:
            sz.write(files, path.basename(files))

    except Exception as e:
        print("Error:", e)


# create_zip(file_path, extract_path + "myProgramOutputpwd.zip", password=True)
# create_7z(file_path, extract_path + "outputFile.7z", password="1234asdf")

extract_7z("/home/pnk/Downloads/outputFile.7z", "/home/pnk/Downloads/")


"""
user input,
input file flexible,
ui,
"""
