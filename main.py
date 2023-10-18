from features.LinearCongruentialGenerator import entry_point as lcg

FEATURES = [
    ("Linear Congruential Generator", lcg.entry_point)
]

def show_menu():
    while True:
        print("Choose the feature")
        for i, (name, func) in enumerate(FEATURES):
            print(f"{i+1}. {name}")
        print("0. Exit")

        try:
            option = int(input("Choice: "))
            if option == 0:
                print("Bye!")
                break

            FEATURES[option - 1][1]()
        except:
            continue

if __name__ == "__main__":
    show_menu()