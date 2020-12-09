import copy
with open('exercise_8_all.txt', "r") as f:
    input_data=f.readlines()

input_data = [[m[:-1], 0] for m in input_data]

print(input_data)
idx=0
visit=0
temp=input_data.copy()
acc=0

def read_ins(ins):
    move=ins[:3]
    sign=ins[4]
    val=ins[5:]
    return move,sign,val

print(temp[idx][1])

def check_one(idx,temp_in):
    idx=idx
    acc=0
    temp=copy.deepcopy(temp_in)
    last=False
    while temp[idx][1]==0:
        move,sign,val = read_ins(temp[idx][0])
        temp[idx][1] = 1
        if idx==len(input_data)-1:
            print("end of table")
            last=True
            break
        # print(temp[idx])
        if idx==617:
            print("previous last=",temp[idx])

        if move=='nop':
            idx+=1
            continue

        if move=='acc':
            if sign=="+":
                acc+=int(val)
                idx+=1
                continue
            elif sign=="-":
                acc-=int(val)
                idx+=1
                continue

        if move=='jmp':
            if int(val) == 0:
                val = 1
            if sign=="+":
                idx+=int(val)
                continue
            elif sign=="-":
                idx-=int(val)
                continue

    return acc,last

def check(idx,temp):
    idx=idx
    acc=0
    try_temp=copy.deepcopy(temp)
    changed=False
    while True:
        move,sign,val = read_ins(temp[idx][0])
        temp[idx][1] = 1
        if move=='nop':
            try_temp[idx][0]=try_temp[idx][0].replace('nop','jmp')
            acc,last = check_one(0,try_temp)
            if last:
                return acc,last

            try_temp[idx][0] = try_temp[idx][0].replace('jmp', 'nop')
            idx+=1
            continue

        if move=='acc':
            if sign=="+":
                acc+=int(val)
                idx+=1
                continue
            elif sign=="-":
                acc-=int(val)
                idx+=1
                continue

        if move=='jmp':
            try_temp[idx][0]=try_temp[idx][0].replace('jmp','nop')
            acc,last = check_one(0,try_temp)
            if last:
                return acc,last

            try_temp[idx][0] = try_temp[idx][0].replace('nop', 'jmp')
            if sign=="+":
                idx+=int(val)
                continue
            elif sign=="-":
                idx-=int(val)
                continue

    return acc,last

print("acc=",check(idx,temp))
print("len=",len(temp))
print(temp[len(input_data)-1])
