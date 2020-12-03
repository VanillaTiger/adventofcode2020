list_numbers =[1721,979,366,299,675,1456]

with open('exercise_1.txt','r') as f:
    list_numbers=f.readlines()

# print(list_numbers)

def find_me(list_numbers):
    for id,val in enumerate(list_numbers):
        if id!=0:
            for x in range(0,id):
                if int(val)+int(list_numbers[x])==2020:
                    return int(val)*int(list_numbers[x])


def find3Numbers(A, arr_size, sum):
    # Fix the first element as A[i]
    for i in range(0, arr_size - 2):

        # Fix the second element as A[j]
        for j in range(i + 1, arr_size - 1):

            # Now look for the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is", A[i],
                          ", ", A[j], ", ", A[k])
                    return True

    # If we reach here, then no
    # triplet was found
    return False

# Driver program to test above function
A = [1, 4, 45, 6, 10, 8]
input = [int(m) for m in list_numbers]
sum = 2020
arr_size = len(input)
find3Numbers(input, arr_size, sum)


print(find_me(list_numbers))