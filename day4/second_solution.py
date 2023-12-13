import argparse
import numpy

"""
Global Variables
"""
filename = "blah"

class Card:
    def __init__(self, input_string) -> None:
        winning_numbers, numbers = Card.parse_input(input_string)
        self.winning_numbers = winning_numbers
        self.numbers = numbers
        self.card_id = Card.get_id(input_string)

    @staticmethod
    def get_id(input_string):
        input_string = input_string.split(":")[0]
        return int(input_string.split("Card ")[1])-1

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
        
        return matches

def process(card_list, count):
    for card in card_list:
        matches = card.process()
        for match in range(matches):
            if (card.card_id+match+1 <= len(card_list)):
                count[card.card_id+match+1] += count[card.card_id]
    print(int(numpy.sum(count)))


def main():
    cards = []
    with open(filename) as file:
        for line in file.readlines():
            cards.append(Card(line))
    counts = numpy.ones(len(cards))
    process(cards, counts)

    """
    Code here
    """

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--real", action='store_true')

    args = parser.parse_args()
    filename = "real_sample.txt" if args.real else "small_sample.txt"
    main()