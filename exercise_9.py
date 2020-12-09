with open('exercise_9_all.txt', 'r') as file:
    input_data = file.readlines()

input_data = [int(m[:-1]) for m in input_data]
print("input_data=",input_data)

preamble = 25


def verify_data(number, previous_data):
    length = len(previous_data)

    sumita = [previous_data[x] + previous_data[y] for x in range(0, length) for y in range(0, length) if x != y]
    if number in sumita: return True


def part1(preamble):
    for i in range(preamble, len(input_data)):
        previous_data = input_data[i - preamble:i]
        valid = verify_data(input_data[i], previous_data)
        if not valid:
            return input_data[i]


def part2(vulnerability):
    length = len(input_data)
    for x in range(0, length):
        sumita = 0
        for y in range(x, length):
            sumita += input_data[y]
            if sumita > vulnerability:
                break
            elif sumita == vulnerability:
                return (x, y)

vulnerability = part1(preamble)
print("vulnerability=",vulnerability)

contigoues_set = part2(vulnerability)
contigoues_set = input_data[contigoues_set[0]:contigoues_set[1]]
print("encryption weakness=",min(contigoues_set) + max(contigoues_set))
