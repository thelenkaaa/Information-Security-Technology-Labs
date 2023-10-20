import os
from .md5_algorithm import MD5

class MD5Service:
    def __init__(self):
        self.md5 = MD5()

        self.message = "Hi, its default message"
        self.result = "There is no hash yet. Use the menu to hash your message/file."

        self.input_file_path = "/Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/features/MD5/input.txt"
        self.output_file_path = "/Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/features/MD5/output.txt"

        print("\nWelcome to MD5")
        print("Default parameters are:")
        print(f"Message: {self.message}\n")


    def read_message_from_terminal(self):
        print("Reading message from terminal")
        self.message = input("Enter new message: ")

    def read_file(self, mode="r"):
        print("Reading the file")
        file_path = input("Enter file path or press Enter to use default filepath: ")
        if not os.path.exists(file_path):
            print(f"File '{file_path}' not found. Reading from {self.input_file_path}")
            file_path = self.input_file_path

        with open(file_path, mode) as file:
            self.message = file.read()
            print("File was successfully read.")

    def read_message_from_file(self):
        self.read_file(mode="r")

    def read_file_as_binary(self):
        self.read_file(mode="rb")

    def write_result_to_file(self):
        print("Writing output to the file")
        file_name = input(f"Enter output file name or press Enter to use default filepath ({self.output_file_path}): ")
        if not file_name:
            print(f"Saving to {self.output_file_path}")
            file_path = self.output_file_path
        else:
            file_path = f"/Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/features/MD5/{file_name}.txt"
            self.output_file_path = file_path
        with open(file_path, "w") as file:
            file.write(self.result)
            print(f"Output was successfully written to {self.output_file_path}.")

    def print_hashed_message(self):
        print("Hashed message is: ", self.result)

    def check_file_integrity(self):
        print("Checking file integrity")
        self.read_file_as_binary()
        self.hash()
        actual_hash = self.result
        print("Actual hash:", actual_hash)
        #9d11c019d3986c013ad0cf15cb1bd39f

        expected_hash = input("Enter the expected MD5 hash: ")

        if actual_hash == expected_hash:
            self.result = "The hashes are equal, file is not corrupted."
        else:
            self.result = "The hashes are not equal, file is corrupted."

        print(self.result)

    def hash(self):
        self.result = self.md5.hexdigest(self.message)
        print("Message has been hashed.")

    def get_features(self):
        features = [
            ("Read message from terminal", self.read_message_from_terminal),
            ("Read message from file", self.read_message_from_file),
            ("Read file for hashing", self.read_file_as_binary),
            ("Hash current message", self.hash),
            ("Check file integrity", self.check_file_integrity),
            ("Write result to file", self.write_result_to_file),
            ("Print hashed message", self.print_hashed_message),
        ]

        return features

    def show_features(self):
        features = self.get_features()
        while True:
            print("Choose the feature")
            for i, (name, func) in enumerate(features):
                print(f"{i+1}. {name}")
            print("0. Exit")

            try:
                option = int(input("Choice: "))
                if option == 0:
                    break

                features[option - 1][1]()
            except:
                print('Entered value does not meet initial requirements! Enter number from 0 to 7!')
                continue


def entry_point():
        service = MD5Service()
        service.show_features()











