import copy

with open('exercise_11_all.txt', 'r') as file:
    input_data = file.readlines()

input_data = [m[:-1] for m in input_data]
input_data = [list(m) for m in input_data]
print(input_data)

rows = len(input_data)
columns = len(input_data[0])
change_seat = True

base_data = copy.deepcopy(input_data)


def check_direction(x, y, m_dif, n_dif):
    m = 1 * m_dif
    n = 1 * n_dif
    while base_data[x + m][y + n] == '.':
        m += m_dif
        n += n_dif
        if rows > x + m >= 0 and columns > y + n >= 0:
            continue
        else:
            return '.'

    return base_data[x + m][y + n]


def check_occupied_2(x, y):
    occupied = 0
    # if (x!=0 and y!=0) and (x!=rows-1 and y!=columns-1):
    for m in range(-1, 2):
        # print("m=",m)
        for n in range(-1, 2):
            # print("n=",n)
            if not (m == 0 and n == 0):
                if rows > x + m >= 0 and columns > y + n >= 0:
                    if check_direction(x, y, m, n) == "#": occupied += 1
    return occupied


def check_occupied(x, y):
    occupied = 0
    # if (x!=0 and y!=0) and (x!=rows-1 and y!=columns-1):
    for m in range(-1, 2):
        # print("m=",m)
        for n in range(-1, 2):
            # print("n=",n)
            if not (m == 0 and n == 0):
                if rows > x + m >= 0 and columns > y + n >= 0:
                    if base_data[x + m][y + n] == "#": occupied += 1
    return occupied


def seat_process():
    seat_moved = False
    for x in range(0, rows):
        for y in range(0, columns):
            if (x == 0 and y == 0) or \
                    (x == rows - 1 and y == columns - 1) or \
                    (x == 0 and y == columns - 1) or (x == rows - 1 and y == 0):
                input_data[x][y] = "#"

            else:
                occupied = check_occupied_2(x, y)
                if base_data[x][y] == '#' and occupied >= 5:
                    seat_moved = True
                    input_data[x][y] = "L"
                if base_data[x][y] == "L" and occupied == 0:
                    input_data[x][y] = "#"
                    seat_moved = True
    return seat_moved


def save_tofile(name):
    with open(f"exercise_11_output_{name}.txt", "w") as file:
        list_of_strings = [''.join(m) for m in input_data]
        file.write('\n'.join(list_of_strings) + '\n')


while change_seat:
    change_seat = seat_process()
    # save_tofile('next')
    base_data = copy.deepcopy(input_data)

print(sum([m.count('#') for m in base_data]))
