with open("exercise_5_all.txt", 'r') as f:
    lines = f.readlines()

print(lines)

def get_seat_id(line):
    #0-127
    row_input=line[0:7]
    column_input=line[7:10]
    bin_rep_row = ""
    bin_rep_col = ""

    for id,let in enumerate(row_input):
        if let=='F':bin_rep_row=bin_rep_row+'0'
        if let =='B':bin_rep_row=bin_rep_row+"1"

    for id,let in enumerate(column_input):
        if let=='L':bin_rep_col=bin_rep_col+'0'
        if let =='R':bin_rep_col=bin_rep_col+"1"

    row = int(bin_rep_row,2)
    column = int(bin_rep_col,2)

    # print(bin_rep_row, int(bin_rep_row,2))
    # print(bin_rep_col, int(bin_rep_col,2))
    seat_id = row*8+column
    # print(seat_id)
    return(seat_id)

all_seats = []
for line in lines:
    all_seats.append(get_seat_id(line))

print("max=",max(all_seats))
print(sorted(all_seats))

all_seasts_sorted=sorted(all_seats)
print(len(all_seasts_sorted))

for id,seat in enumerate(all_seasts_sorted):
    if seat != all_seasts_sorted[id+1]-1:
        print(seat)


