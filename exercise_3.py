with open("exercise_3.txt",'r') as f:
    input_list = f.readlines()

input_list = [m.rstrip('\n') for m in input_list]
# print(input_list[-1])
right=3
down=1
previous=0
trees=0

for id,line in enumerate(input_list):
    # if id%2==0:
        if id==0:
            previous=0
        if id!=0:
            while previous+right >= len(line):
                line=line+line

            print('found=',line[previous+right])
            line = list(line)
            if line[previous+right]=='#':
                trees+=1
                line[previous+right]='X'
            else:
                line[previous+right]='O'
            print("".join(line))
            previous=previous+right


print(trees)

#84
#195
#70
#70
#47