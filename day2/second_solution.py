from enum import Enum
import numpy


class Colour(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2


class Game:
    def __init__(self, game_string) -> None:
        game_id, rounds = Game.parse_game_string(game_string)
        self.game_id = game_id
        self.rounds = rounds

    def parse_game_string(game_string):
        game_string = game_string[5:]
        idx, game_string = game_string.split(": ")

        rounds = game_string.split(";")
        round_scores = []
        for game_round in rounds:
            round_scores.append(Game.parse_round_string(game_round))

        return (int(idx), round_scores)
    
    def parse_round_string(round_string):
        red = blue = green = 0
        colours = round_string.replace(" ", "").split(",")
        for colour in colours:
            if ("red" in colour):
                red = int(colour.replace("red", ""))
            elif ("blue" in colour):
                blue = int(colour.replace("blue", ""))
            elif ("green" in colour):
                green = int(colour.replace("green", ""))
        return numpy.array([red, blue, green])

    def validate(self, maximum_scores):
        for game_round in self.rounds:
            output = numpy.subtract(maximum_scores, game_round)
            if (numpy.any((output < 0))):
                return 0
        return self.game_id
    
    def minimum_values(self):
        min_red = min_blue = min_green = 0
        for game_round in self.rounds:
            if game_round[Colour.RED.value] > min_red:
                min_red = game_round[Colour.RED.value]
            if game_round[Colour.BLUE.value] > min_blue:
                min_blue = game_round[Colour.BLUE.value]
            if game_round[Colour.GREEN.value] > min_green:
                min_green = game_round[Colour.GREEN.value]
        return min_red * min_blue * min_green

games = []
with open("day2/real_sample.txt") as file:
    for line in file.readlines():
        games.append(Game(line))

score_max = numpy.array([12, 14, 13])
total = 0
for game in games:
    total += game.minimum_values()

print(total)