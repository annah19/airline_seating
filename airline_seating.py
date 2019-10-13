
SEAT_COL = ['A','B','C','D','E','F','G','H','I','J']

def get_number_of_rows():
    ''' returns a number of rows '''
    rows = int(input("Enter number of rows: "))

    return rows

def get_number_of_seats():
    ''' returns a number of seats '''
    seats = int(input("Enter number of seats in each row: "))

    return seats

def data_list(seats,rows):

    seat_list = SEAT_COL[:seats]
    row_list = []
    for i in range(0,rows):
        row_list.append(seat_list)

    return row_list

def print_plane(row_list):
    '''Take the list of lists, prints out the seats 
    in the plane with spaces and aisle'''

    # For every row 
    for i in range(0,len(row_list)):
        print("{:>2d}".format(i+1),end="   ")

        # For every seat
        for x in range(0, len(row_list[i])):
            print(row_list[i][x], end=" ")

            # Find the middle in the seats
            if (len(row_list[i])-1) // 2 == x:
                print(end=" ")
        

        print()

    return


def reserve_seat(row,seat,row_list):
    
    for i in range(0,len(row_list)):
        if (i-1) == int(row):
            # 
            for x in range(0,len(row_list[i])):
                if row_list[i][x] == seat:
                    row_list[i][x] = "X"

    return row_list







def main():
    seats = get_number_of_seats()
    rows = get_number_of_rows()

    row_list = data_list(rows,seats)

    print_plane(row_list)
    while True:
        more_seats = input("More seats (y/n)? ")

        if more_seats == "y":
            row_seat = input("Input seat number (row seat): ")
            row_seat = row_seat.split()
            row_list = reserve_seat(row_seat[0],row_seat[1],row_list)
            print_plane(row_list)
                #     print("That seat is taken!")
                # # ef sæti er ekki til
                #     print("Seat number is invalid!")

    # else:
    #     break

main()