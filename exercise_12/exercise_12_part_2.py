with open('exercise_12_all.txt', 'r') as file:
    input_data=file.readlines()

input_data = [m[:-1] for m in input_data]

print(input_data)

waypoint_pos = {'E':10,'W':0,'N':1,'S':0}
new_waypoint_pos = {'E':0,'W':0,'N':0,'S':0}
ship_pos = {'E':0,'W':0,'N':0,'S':0}

possible_directions = ['N','E','S','W']

for item in input_data:
    new_waypoint_pos = {'E': 0, 'W': 0, 'N': 0, 'S': 0}
    if item[0] in waypoint_pos.keys():
        if item[0]=='W':
            if waypoint_pos['E']==0: waypoint_pos['W']+=int(item[1:])
            else:
                diff= waypoint_pos['E']-int(item[1:])
                if diff>0:
                    waypoint_pos['E'] = diff
                else:
                    waypoint_pos['W'] = abs(diff)
                    waypoint_pos['E'] = 0
        if item[0]=='E':
            if waypoint_pos['W']==0: waypoint_pos['E']+=int(item[1:])
            else:
                diff= waypoint_pos['W']-int(item[1:])
                if diff>0:
                    waypoint_pos['W'] = diff
                else:
                    waypoint_pos['E'] = abs(diff)
                    waypoint_pos['W']=0
        if item[0]=='N':
            if waypoint_pos['S']==0: waypoint_pos['N']+=int(item[1:])
            else:
                diff= waypoint_pos['S']-int(item[1:])
                if diff>0:
                    waypoint_pos['S'] = diff
                else:
                    waypoint_pos['N'] = abs(diff)
                    waypoint_pos['S'] = 0
        if item[0]=='S':
            if waypoint_pos['N']==0: waypoint_pos['S']+=int(item[1:])
            else:
                diff= waypoint_pos['N']-int(item[1:])
                if diff>0:
                    waypoint_pos['N'] = diff
                else:
                    waypoint_pos['S'] = abs(diff)
                    waypoint_pos['N'] = 0


    if item[0]=='R':
        for k in waypoint_pos.keys():
            if waypoint_pos[k]!=0:
                index=possible_directions.index(k)
                index+=int(item[1:])//90
                index=index%4
                direction=possible_directions[index]
                new_waypoint_pos[direction]=waypoint_pos[k]
        waypoint_pos=new_waypoint_pos

    if item[0]=='L':
        for k in waypoint_pos.keys():
            if waypoint_pos[k]!=0:
                index = possible_directions.index(k)
                index-=int(item[1:])//90
                index=index%4
                direction=possible_directions[index]
                new_waypoint_pos[direction]=waypoint_pos[k]
        waypoint_pos=new_waypoint_pos

    if item[0]=='F':
        for k in waypoint_pos.keys():
            if waypoint_pos[k]!=0:
                ship_pos[k]+=int(item[1:])*waypoint_pos[k]

position = abs(ship_pos['E']-ship_pos['W'])+abs(ship_pos['N']-ship_pos['S'])

print(ship_pos)
print(position)