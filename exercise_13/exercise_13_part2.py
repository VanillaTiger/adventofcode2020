from functools import reduce

# oblicza NWD (najwiekszy wspolny dzielnik) dla dwoch liczb
def gcd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


# oblicza NWW (najmniejsza wspolna wielokrotnosc) dla dwoch liczb
def lcm(a, b):
    """
    lcm(3, 8) => 24
    """
    return abs(a * b / gcd(a, b))


# oblicza NWW (najmniejsza wspolna wielokrotnosc) dla listy liczb
def lcm_list(l):
    """
    lcm_list([3, 4, 5, 6]) => 60
    """
    return reduce(lcm, l, 1)

with open('exercise_13_all.txt', 'r') as file:
    earliest=file.readline()
    bus_ids=file.readline()

bus_ids=bus_ids.split(',')
bus_indx=[(m,bus_ids.index(m)) for m in bus_ids if m!='x']
print(bus_indx)
index = 2
increment=int(bus_indx[0][0])
timestamp=int(bus_indx[0][0])

while index<=len(bus_indx):
    temp_timestamp=timestamp
    valid=False
    for id,item in enumerate(bus_indx[:index]):
        temp_timestamp = timestamp + item[1]
        if item!='x':
            # print(f"for {timestamp} mod{item} equal to {int(item)%temp_timestamp}")
            if temp_timestamp%int(item[0])==0:
                valid=True
            else:
                valid=False

    if valid==True:
        print(timestamp)
        increment = lcm_list(int(i[0]) for i in bus_indx[:index])
        timestamp += increment
        index+=1
    else:
        timestamp += increment

#554865447501099