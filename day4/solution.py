import argparse

"""
Global Variables
"""
filename = "blah"

class Card:
    def __init__(self, input_string) -> None:
        winning_numbers, numbers = Card.parse_input(input_string)
        self.winning_numbers = winning_numbers
        self.numbers = numbers

    @staticmethod
    def parse_input(input_string):
        input_string = input_string.split(":")[1]
        input_string = " ".join(input_string.split())
        input_string = input_string.split(" | ")
        winning_numbers = input_string[0].split()
        numbers = input_string[1].split()
        return (winning_numbers, numbers)
    
    def process(self):
        matches = 0
        for number in self.winning_numbers:
            matches += self.numbers.count(number)
        
        if matches == 0: return 0
        return 2 ** (matches-1)


def main():
    total = 0
    with open(filename) as file:
        for line in file.readlines():
            total += Card(line).process()
    print(total)

    """
    Code here
    """

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--real", action='store_true')

    args = parser.parse_args()
    filename = "real_sample.txt" if args.real else "small_sample.txt"
    main()