import zipfile
import getpass
import os
import py7zr


def extract_zip(zip_file_path, extraction_path):

    os.makedirs(extraction_path, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        try:

            zip_ref.extractall(extraction_path)
            print("Success: Extracted without a password!")

        except RuntimeError as e:
            error_msg = str(e).lower()

            if "password required" in error_msg or "encrypted" in error_msg:
                print("Lock detected: This ZIP file is password protected.")

                while True:

                    pwd = getpass.getpass(
                        "Enter password (or press Ctrl+C to cancel): "
                    )

                    try:

                        zip_ref.extractall(extraction_path, pwd=pwd.encode("utf-8"))
                        print("Success: Password accepted and files extracted!")
                        break

                    except RuntimeError as pwd_error:
                        if "bad password" in str(pwd_error).lower():
                            print("Incorrect password. Please try again.\n")
                        else:
                            print(f"An unexpected error occurred: {pwd_error}")
                            break
            else:
                print(f"Extraction failed: {e}")


def extract_7z(archive_path, extraction_path):
    os.makedirs(extraction_path, exist_ok=True)

    try:

        with py7zr.SevenZipFile(archive_path, mode="r") as z:
            if z.needs_password():
                print("Lock detected: This 7z file is password protected.")

                while True:
                    pwd = getpass.getpass(
                        "Enter password (or press Ctrl+C to cancel): "
                    )

                    try:

                        with py7zr.SevenZipFile(
                            archive_path, mode="r", password=pwd
                        ) as z_pwd:
                            z_pwd.extractall(path=extraction_path)

                        print("Success: Password accepted and files extracted!")
                        break

                    except py7zr.exceptions.BadPassword:
                        print("Incorrect password. Please try again.\n")
                    except Exception as pwd_error:
                        print(f"An unexpected error occurred: {pwd_error}")
                        break
            else:
                # No password needed
                z.extractall(path=extraction_path)
                print("Success: Extracted without a password!")

    except Exception as e:
        print(f"Extraction failed: {e}")


def extract_rar(rar_file_path, extraction_path):
    os.makedirs(extraction_path, exist_ok=True)

    try:
        with rarfile.RarFile(rar_file_path, "r") as rf:

            if rf.needs_password():
                print("Lock detected: This RAR file is password protected.")

                while True:
                    pwd = getpass.getpass(
                        "Enter password (or press Ctrl+C to cancel): "
                    )

                    try:

                        rf.extractall(path=extraction_path, pwd=pwd)
                        print("Success: Password accepted and files extracted!")
                        break

                    except rarfile.BadRarFile as pwd_error:
                        print(
                            "Incorrect password or corrupted file. Please try again.\n"
                        )

                    except rarfile.Error as pwd_error:
                        error_msg = str(pwd_error).lower()

                        if (
                            "bad password" in error_msg
                            or "password" in error_msg
                            or "crc" in error_msg
                        ):
                            print("Incorrect password. Please try again.\n")
                        else:
                            print(f"An unexpected error occurred: {pwd_error}")
                            break
            else:
                rf.extractall(path=extraction_path)
                print("Success: Extracted without a password!")

    except rarfile.Error as e:
        print(f"Extraction failed: {e}")
    except FileNotFoundError:
        print(f"Error: The file {rar_file_path} was not found.")


# extract_smart("example.zip", "extracted_files/")
