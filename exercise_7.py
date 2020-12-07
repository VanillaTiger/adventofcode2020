with open('exercise_7_all.txt','r') as file:
    lines = file.readlines()

lines = [x[:-2] for x in lines]
# print(lines)

database = {}
suma = 0

def create_base():
    for line in lines:
        content=line.split('contain')
        content = [m.replace('bags','bag') for m in content]
        inside = content[1].split(',')
        inside = [m.replace('bags', 'bag') for m in inside]
        list_inside=[[(' ').join(m.split()[1:]),m.split()[0]] for m in inside]
        database[content[0][:-1]]=list_inside

    database['other bag']= ""
    print(database)
    # quit()


def find_shiny(data, found):
    for v in data:
        if v[0] == 'shiny gold bag':
            found =True
            break
        if found !=True:
            found=find_shiny(database[v[0]],found)
    if found==True:
        return (found)


def part1(suma):
    for k,v in database.items():
        valid = find_shiny(v, False)
        if valid:
            suma+=1
            # print(k,v)

    print(suma)

def find_bags(bag,result=1):
    for bags in database[bag]:
        if bags[0] == "other bag":
            return 1
        result+=int(bags[1])*find_bags(bags[0])
    return result


create_base()
part1(suma)
print(find_bags("shiny gold bag")-1)
