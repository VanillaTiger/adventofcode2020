with open("exercise_6_all.txt", 'r') as f:
    lines = f.readlines()

print(lines)
person = []
group = []
compare = []
sum = 0

for item in lines:
    # print(item)
    if item=="\n":
        # print("group=",len(group))
        if len(group) == 1:
            compare = set(group[0])
        else:
            for i in range(0,len(group)):
                # print(i)
                if i==0:
                    compare = set(group[0])
                else:
                    compare = set(compare)&set(group[i])
        sum+=len(set(compare))
        # print("compare=",compare)
        # print("sum=",sum)
        # print(sum)
        group=[]
        compare=[]
    else:
        item = item[:-1]
        person=[]
        for letter in item:
            # print(letter)
            person.append(letter)
        group.append(person.copy())
print(sum)