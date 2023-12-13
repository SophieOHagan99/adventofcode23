import re
total = 0

number_list = [
    "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]

number_replacement = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

noChars = []
def process(line):
    for i in range(len(number_list)):
        line = line.replace(number_list[i], number_replacement.get(number_list[i]))
    noChars.append(re.sub(r"[a-zA-Z\n]", "", line))
    line = list(filter(type(line).isdigit, line))
    return int(line[0]+line[-1])


with open("day1/realsample.txt") as file:
    for line in file.readlines():
        total += process(line)
    int_list = []
    for i in noChars:
        int_list.append(int(i[0]+i[-1]))
    print(sum(int_list))

print(total)
