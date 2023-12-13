from dataclasses import dataclass
import numpy

special_characters = "!@#$%^&*()-+?_=,<>/"

@dataclass
class PartLocation:
    x_coord: int
    y_coord: int
    length: int
    gear: bool = False
    value: int = 0

    def x_set(self):
        return set(range(self.x_coord, self.x_coord+self.length))

class EngineSchematic:
    def __init__(self) -> None:
        self.schematic = []
        self.numeric_parts = []
        self.non_numeric_parts = {}
        self.valid_parts = []
        self.gear_locations = []
        self.numeric_part_dict = {}

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
                elif line[i] == "*":
                    self.gear_locations.append(PartLocation(i, y, 1, True))
                    symbol_locations.append(i)
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
        valid_parts = []
        for part in self.numeric_parts:
            possible_y_coords = self.get_possible_y_coords(part)
            possible_x_coords = self.get_possible_x_coords(part)
            for y in possible_y_coords:
                values = set(self.non_numeric_parts.get(y))
                coords_to_check = set(possible_x_coords)
                if (values & coords_to_check):
                    part.value = int(self.schematic[part.y_coord][part.x_coord:part.x_coord+part.length])
                    if(self.numeric_part_dict.get(part.y_coord)):
                        temp = self.numeric_part_dict.get(part.y_coord)
                        temp.append(part)
                        self.numeric_part_dict.update({part.y_coord: temp})
                    else:
                        self.numeric_part_dict.update({part.y_coord: [part]})
                    valid_parts.append(part)
                    break
        self.valid_parts = valid_parts

    def get_adjacent_parts(self, gear):
        possible_y_coords = self.get_possible_y_coords(gear)
        possible_x_coords = self.get_possible_x_coords(gear)
        adjacent_parts = []
        for y in possible_y_coords:
            x = self.numeric_part_dict.get(y)
            if not x:
                continue
            for part in x:
                part_set = part.x_set()
                gear_set = set(possible_x_coords)
                if (part_set & gear_set):
                    adjacent_parts.append(part.value)
        return adjacent_parts

    def find_gear_ratios(self):
        total = 0
        for gear in self.gear_locations:
            adjacent_parts = self.get_adjacent_parts(gear)
            if len(adjacent_parts) == 2:
                total += adjacent_parts[0] * adjacent_parts[1]
        print(total)


schematic = EngineSchematic()

with open("day3/real_sample.txt") as file:
    for line in file.readlines():
        schematic.append_schematic(line)

test_line = "467..114.."
schematic.find_parts()
schematic.validate_parts()
schematic.find_gear_ratios()