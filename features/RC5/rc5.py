import os

from .rc5_algorithm import RC5
from features.MD5.md5 import MD5


class RC5_SERVICE():
    def __init__(self):
        self.md5 = MD5()
        self.input_file = "/Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/features/RC5/input.txt"
        self.output_file = "/Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/features/RC5/result.txt"

        self.word_size = 16
        self.num_rounds = 12
        self.passcode = "Default passcode"
        self.key = self.md5.hexdigest(self.passcode).encode('utf-8')
        self.service = RC5(self.key, self.word_size, self.num_rounds)

        print("Welcome to RC5\n")
        print("Default parameters are:")
        print(f"Word size: {self.word_size}")
        print(f"Rounds: {self.num_rounds}")
        print(f"Passcode: {self.passcode}")
        print(f"Input file path: {self.input_file}")
        print(f"Output file path: {self.output_file}")
        print()

    def decrypt(self):
        print("Decrypting file")
        input_file_path = input(f"Enter input file path or press Enter to use default file {self.output_file}: ")
        if not input_file_path or not os.path.exists(input_file_path):
            input_file_path = self.output_file

        output_file_path = input(f"Enter output file path or press Enter to use default file {self.input_file}: ")
        if not output_file_path:
            output_file_path = self.input_file

        print("Decryption in progress...")
        self.service.decrypt_file(input_file_path, output_file_path)

        print("Decryption successful! Decrypted data saved to", output_file_path)

    def encrypt(self):
        print("Encrypting file")
        input_file_path = input(f"Enter input file path or press Enter to use default file {self.input_file}: ")
        if not input_file_path or not os.path.exists(input_file_path):
            input_file_path = self.input_file

        # Check file size
        file_size = os.path.getsize(input_file_path) / (1024 * 1024)  # File size in MB
        if file_size > 10:
            print("Error: File size is more than 2 MB. Please select a smaller file.")
            return

        output_file_path = input(f"Enter output file path or press Enter to use default file {self.output_file}: ")

        if not output_file_path:
            print(f"Saving to {self.output_file}")
            output_file_path = self.output_file

        print("Encryption in progress...")
        self.service.encrypt_file(input_file_path, output_file_path)

        print("Encryption successful! Encrypted data saved to", output_file_path)

    def get_available_features(self):
        available_features = [
            ("Encrypt file", self.encrypt),
            ("Decrypt file", self.decrypt),
        ]
        return available_features

    def show_initial_options(self):
        features = self.get_available_features()
        while True:
            print("Choose the option:")
            for i in range(len(features)):
                print(f"{i + 1}. {features[i][0]}")
            print("0. Exit")

            try:
                option = int(input("Option: "))
                if option == 0:
                    return False

                print()
                features[option - 1][1]()
                os.system("clear")
            except Exception as e:
                print(e)
                continue

def entry_point():
    service = RC5_SERVICE()
    while True:
        if not service.show_initial_options():
            break

# Input         /Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/song.m4a
# Encryption    /Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/features/RC5/result-enc.m4a
# Decryption    /Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/features/RC5/result-dec.m4a