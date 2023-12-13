from dataclasses import dataclass

special_characters = "!@#$%^&*()-+?_=,<>/"

@dataclass
class PartLocation:
    x_coord: int
    y_coord: int
    length: int

class EngineSchematic:
    def __init__(self) -> None:
        self.schematic = []
        self.numeric_parts = []
        self.non_numeric_parts = {}

    def append_schematic(self, line):
        self.schematic.append(line)

    def find_parts(self):
        y = 0
        for line in self.schematic:
            i = 0
            j = 0
            symbol_locations = []
            while i < len(line):
                if line[i] == ".":
                    pass
                elif line[i].isnumeric():
                    j = i
                    while (line[j].isnumeric()):
                        if (j == len(line)):
                            break
                        j += 1
                    self.numeric_parts.append(PartLocation(i, y, (j - i)))
                    i = j - 1
                elif line[i] in (special_characters):
                    symbol_locations.append(i)
                i += 1
            self.non_numeric_parts.update({y: symbol_locations})
            y += 1

    def get_possible_y_coords(self, part: PartLocation):
        if part.y_coord == 0:
            return [0, 1]
        elif part.y_coord == (len(self.schematic)-1):
            return [part.y_coord - 1, part.y_coord]
        else:
            return [part.y_coord-1, part.y_coord, part.y_coord+1]
        
    def get_possible_x_coords(self, part: PartLocation):
        coords = range(part.x_coord-1, part.x_coord+part.length+1)
        return list(filter(lambda x:((x >= 0) and (x <= len(self.schematic[0]))), coords))

    def validate_parts(self):
        total = 0
        for part in self.numeric_parts:
            possible_y_coords = self.get_possible_y_coords(part)
            possible_x_coords = self.get_possible_x_coords(part)
            for y in possible_y_coords:
                values = set(self.non_numeric_parts.get(y))
                coords_to_check = set(possible_x_coords)
                if (values & coords_to_check):
                    total += int(self.schematic[part.y_coord][part.x_coord:part.x_coord+part.length])
                    break
        print(total)

schematic = EngineSchematic()

with open("day3/real_sample.txt") as file:
    for line in file.readlines():
        schematic.append_schematic(line)

test_line = "467..114.."
schematic.find_parts()
schematic.validate_parts()