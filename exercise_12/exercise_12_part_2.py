with open('exercise_12_all.txt', 'r') as file:
    input_data = file.readlines()

input_data = [m[:-1] for m in input_data]

print(input_data)

waypoint_pos = {'E': 10, 'W': 0, 'N': 1, 'S': 0}
ship_pos = {'E': 0, 'W': 0, 'N': 0, 'S': 0}

possible_directions = ['N', 'E', 'S', 'W']
possible_rotations = ['R', 'L']


def move_waypoint(item):
    direction = item[0]
    opposite_direction = possible_directions[possible_directions.index(direction) - 2]

    if item[0] == direction:
        if waypoint_pos[opposite_direction] == 0:
            waypoint_pos[direction] += int(item[1:])
        else:
            diff = waypoint_pos[opposite_direction] - int(item[1:])
            if diff > 0:
                waypoint_pos[opposite_direction] = diff
            else:
                waypoint_pos[direction] = abs(diff)
                waypoint_pos[opposite_direction] = 0

    return waypoint_pos


def rotate(item):
    rotation=item[0]
    new_waypoint_pos = {'E': 0, 'W': 0, 'N': 0, 'S': 0}
    for k in waypoint_pos.keys():
        if waypoint_pos[k] != 0:
            index = possible_directions.index(k)
            if rotation == 'R':
                index += int(item[1:]) // 90
            if rotation == 'L':
                index -= int(item[1:]) // 90
            index = index % 4
            direction = possible_directions[index]
            new_waypoint_pos[direction] = waypoint_pos[k]
    return new_waypoint_pos


for item in input_data:

    if item[0] in possible_directions:
        waypoint_pos = move_waypoint(item)

    if item[0] in possible_rotations:
        waypoint_pos = rotate(item)

    if item[0] == 'F':
        for k in waypoint_pos.keys():
            if waypoint_pos[k] != 0:
                ship_pos[k] += int(item[1:]) * waypoint_pos[k]

position = abs(ship_pos['E'] - ship_pos['W']) + abs(ship_pos['N'] - ship_pos['S'])

print(ship_pos)
print(f"manhattan distance = {position}")
