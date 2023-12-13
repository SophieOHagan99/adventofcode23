total = 0


def process(line):
    line = list(filter(type(line).isdigit, line))
    return int(line[0]+line[-1])


with open("day1/realsample.txt") as file:
    for line in file.readlines():
        total += process(line)
print(total)

