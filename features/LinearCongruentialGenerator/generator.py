class Generator:
    def __init__(self, a, x, c, m):
        self.a = a
        self.x = x
        self.c = c
        self.m = m

    def generate_value(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    @staticmethod
    def get_period(sequence):
        seq = set(sequence)
        return len(seq)

    @staticmethod
    def show_values(a, x, c, m):
        print("Here are default values for generator:")
        print("Generator Parameters:")
        print(f"Factor (a):\t\t\t\t{a}")
        print(f"Initial Number (x):\t\t{x}")
        print(f"Increment (c):\t\t\t{c}")
        print(f"Comparison Module (m):\t{m}")


    def get_generated_sequence(self):
        correct = False
        while not correct:
            try:
                l = int(input("Enter sequence length: "))
                correct = True
            except ValueError:
                print("Entered value does not meet initial requirements! Enter number!")

        sequence = []
        x = self.x
        for i in range(l):
            sequence.append(x)
            x = self.generate_value()

        period = self.get_period(sequence)

        return sequence, period
