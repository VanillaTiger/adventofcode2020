with open('exercise_10_all.txt', 'r') as file:
    input_data=file.readlines()

input_data = [int(m[:-1]) for m in input_data]
input_data=sorted(input_data)
print(input_data)
volume = {"0":0,"1":0,"2":0,"3":0}

def part1():

    for i in range(0,len(input_data)):
        volume[str(input_data[i+1]-input_data[i])]+=1

    print(volume)


def part2():
    combination = 1
    comb_temp = 0
    multiplicator=[1,1,2,4,7]
    for i in range(0,len(input_data)-1):
        if input_data[i+1]-input_data[i]==1:
            comb_temp+=1
        else:
            combination*=multiplicator[comb_temp]
            comb_temp=0
    print(combination)
part2()