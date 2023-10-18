try:
    from features.LinearCongruentialGenerator.config import a, x, c, m
    from features.LinearCongruentialGenerator.generator import Generator
except ImportError as e:
    print(f"Error importing necessary modules: {e}")
    exit()


def show_values(a, x, c, m):
    print("Here are default values for generator:")
    print("Generator Parameters:")
    print(f"Factor (a):\t\tt{a}")
    print(f"Initial Number (x):\t{x}")
    print(f"Increment (c):\t\t{c}")
    print(f"Comparison Module (m):\t{m}")


def entry_point():
    proceed = True
    print("\nWelcome to Linear Congruential Generator!")
    while proceed == True:
        print("\nChoose what to do:\n\n"
              "Generate sequence and count its period, print output to console, press 1\n"
              "\nGenerate sequence and count its period, write output to file, press 2\n"
              "\nGenerate sequence and count its period, write output to file and to console, press 3\n"
              "\nShow default values for generator, press 4\n"
              "\nExit, press 5")
        correct = False
        case_value = 0
        while not correct:
            try:
                print("\nEnter your option:")
                case_value = int(input())
                correct = True
                if case_value > 5:
                    print("There is no such option!")
                    correct = False
            except ValueError:
                print("Entered value does not meet initial requirements! Enter number from 1 to 5!")

        generator = Generator(a, x, c, m)
        if case_value < 4:
            sequence, period = generator.get_generated_sequence()
            if case_value == 1:
                print("Here is the output:")
                print(f"Generated sequence: {sequence}")
                print(f"Period: {period}")
            elif case_value == 2:
                filename = input("Enter filename:")
                print(f"Results were written to /Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/{filename}.txt file")
                f = open(f'{filename}.txt', 'w')
                f.write(f'\nSequence:\n{sequence}')
                f.write(f'\nPeriod: {period}')
                f.close()
            elif case_value == 3:
                filename = input("Enter filename:")
                print("Here is the output:")
                print(f"Generated sequence: {sequence}")
                print(f"Period: {period}")
                print(f"Results were also written to /Users/lenka/Documents/Fifth semester/TofSI/Лаба 1/{filename}.txt file")
                f = open(f'{filename}.txt', 'w')
                f.write(f'\nSequence:\n{sequence}')
                f.write(f'\nPeriod: {period}')
                f.close()
        elif case_value == 4:
            show_values(a, x, c, m)
        else:
            # print("Have a good day :) U exited the program")
            proceed = False
