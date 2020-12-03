"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

with open("exercise_2.txt",'r') as f:
    input_list=f.readlines()

input_list = [m[:-1] for m in input_list]
# print(input_list)

# input_list=["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

output = 0

for i in input_list:
    numbers=i.split()
    number_a = int(numbers[0].split('-')[0])
    number_b = int(numbers[0].split('-')[1])
    to_find = numbers[1][0]
    password = numbers[2]
    # print(number_a, number_b, to_find,password)
    # print(password.count(to_find))

    # if number_a<= password.count(to_find)<= number_b:
    #     output+=1

    if to_find==password[number_a-1]:
        if to_find!=password[number_b-1]:
            output+=1
    else:
        if to_find==password[number_b-1]:
            output+=1

print(output)