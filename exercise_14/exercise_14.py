def get_result_after_mask(value,mask):
    result = ''
    for idx,item in enumerate(value):
        if mask[idx]!='X':
            result+=mask[idx]
        else:
            result+=item
    return result

def get_memory_after_mask(value,mask):
    result = ''
    lista_memories = []
    for idx,item in enumerate(value):
        if mask[idx]!='X':
            result+=mask[idx]
        else:
            result+='X'
    return  result

def create_memory(list_memories):
    temp = list_memories.copy()
    mix=False
    for turn,memory in enumerate(temp):
        for idx,item in enumerate(memory):
            if item == 'X':
                to_change=list(memory)
                to_change[idx] = '0'
                temp.append(''.join(to_change))
                to_change[idx] = '1'
                temp.append(''.join(to_change))

    temp =set(temp)
    temp=list(temp)
    temp=[m for m in temp if 'X' not in m]
    print('temp=',temp)
    return temp

# create_memory(['000000000000000000000000000000X1101X'])

def part1():
    f=open("exercise_14_all.txt",'r')
    mask=''
    memory={}
    while True:
        line=f.readline()
        if not line:
            break

        input_data=line.split()
        if input_data[0]=='mask':
            mask=input_data[2]
        if input_data[0][:3]=='mem':
            value='{0:036b}'.format(int(input_data[2]))
            memory[input_data[0][3:-1]]=get_result_after_mask(value,mask)

    sumita = 0

    for k,v in memory.items():
        number=int(v, 2)
        if number!=0:
            sumita+=number

    print(sumita)

# part1()

def part2():
    sumita=0
    f=open("exercise_14_part2.txt",'r')
    mask=''
    memory={}
    while True:
        line=f.readline()
        if not line:
            break

        input_data=line.split()
        if input_data[0]=='mask':
            mask=input_data[2]
        if input_data[0][:3]=='mem':
            mem= int(input_data[0][4:-1])
            number = input_data[2]
            value='{0:036b}'.format(mem)
            floating_memory=get_memory_after_mask(value,mask)
            all_memories=create_memory([floating_memory])
            for mem in all_memories:
                memory[mem]=number



    print(sumita)
    print((memory))
    some=[[int(k, 2),v] for k,v in memory.items()]

    print(some)
    for k,v in memory.items():
        sumita+=int(v)

part2()