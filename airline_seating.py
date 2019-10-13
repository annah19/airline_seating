
SEAT_COL = ['A','B','C','D','E','F','G','H','I','J']

def get_number_of_rows():
    ''' returns a number of rows '''
    rows = int(input("Enter number of rows: "))

    return rows

def get_number_of_seats():
    ''' returns a number of seats '''
    seats = int(input("Enter number of seats in each row: "))

    return seats

def data_list(rows,seats):

    row_list = []
    for i in range(0,rows):
        row_list.append(SEAT_COL[:seats])

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

def is_seat_reserved(row,seat,row_list):
    
    pass


def reserve_seat(row,seat,row_list,reserved_seats):

    for i in range(0,len(row_list)):

        if i == row-1:
            for x in range(0,len(row_list[i])):
                if row_list[i][x] == seat:
                    row_list[i][x] = "X"
                    reserved_seats.append((row,seat))

    return row_list,reserved_seats







def main():
    rows = get_number_of_rows()
    seats = get_number_of_seats()

    row_list = data_list(rows,seats)
    reserved_seats = []

    print_plane(row_list)
    while True:
        more_seats = input("More seats (y/n)? ")

        if more_seats == "y":
            row_seat = input("Input seat number (row seat): ")
            row_seat = row_seat.split()

            row = int(row_seat[0])
            seat = row_seat[1]
            
            if (row,seat) in reserved_seats:
                print("That seat is taken!")
                continue

            if (len(row_list) < row or seat not in row_list[row-1]):
                print("Seat number is invalid!")
                continue

            reserve_seat_results = reserve_seat(row,seat,row_list,reserved_seats)
            row_list = reserve_seat_results[0]
            reserved_seats = reserve_seat_results[1]

            print_plane(row_list)
                #     print("That seat is taken!")
                # # ef sæti er ekki til
                #     print("Seat number is invalid!")

        else:
            break

main()