with open('exercise_13_all.txt','r') as file:
    earliest=file.readline()
    bus_ids=file.readline()

    earliest=earliest[:-1]
    bus_ids=bus_ids.split(',')
def part1(earliest,bus_ids):
    print(earliest)
    print(bus_ids)
    bus_ids=list(filter(lambda a: a != 'x', bus_ids))

    leave = [int(earliest)//int(item) for item in bus_ids if item!='x']

    smallest= leave.index(min(leave))
    print(leave.index(min(leave)))
    bus=int(bus_ids[smallest])
    earliest=int(earliest)

    time=((bus*min(leave)+bus)-earliest)*bus
    print(time)

part1(earliest,bus_ids)



