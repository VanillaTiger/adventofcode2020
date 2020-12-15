with open('exercise_15_all.txt','r') as file:
    input_data=file.readline()

input_data=input_data.split(',')
input_data=[int(m) for m in input_data]
print(input_data)
last_visited={}

last_spoken = input_data[0]

for idx,item in enumerate(input_data):
    last_visited[item]=idx+1
    last_spoken=item

last_spoken=0
numbers=len(input_data)

for turn in range(numbers+1,30000001):
    if turn == 30000000 : print("last=",last_spoken)
    if last_spoken not in last_visited.keys():
        last_visited[last_spoken]=turn
        last_spoken=0
        continue

    if last_spoken in last_visited.keys():
        new_last_spoken = turn - last_visited[last_spoken]
        last_visited[last_spoken] = turn
        last_spoken=new_last_spoken