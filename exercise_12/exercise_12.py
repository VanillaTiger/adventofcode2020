with open('exercise_12_all.txt', 'r') as file:
    input_data=file.readlines()

input_data = [m[:-1] for m in input_data]

print(input_data)

moves = {'E':0,'W':0,'N':0,'S':0}

direction = 'E'
possible_directions = ['N','E','S','W']
index=1

for item in input_data:
    if item[0] in moves.keys():
        moves[item[0]]+=int(item[1:])

    if item[0]=='R':
        index+=int(item[1:])//90
        index=index%4
        direction=possible_directions[index]

    if item[0]=='L':
        index-=int(item[1:])//90
        index=index%4
        direction=possible_directions[index]

    if item[0]=='F':
        moves[direction]+=int(item[1:])

position = abs(moves['E']-moves['W'])+abs(moves['N']-moves['S'])

print(moves)
print(position)