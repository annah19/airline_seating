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
    '''Take in the row and seat from the user 
    and return a list of list with seatnumber row-times'''

    row_list = []

    for i in range(0,rows):

        # We only need the seats in the list that the user asks for
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
                print(end="  ")
        
        print()

    return


def reserve_seat(row_seat,row_list,reserved_seats):
    '''Checks if the seat is already taken or if 
        the seat number is in the input from the user. 
        Updates the row_list and reserved_seats list'''

    # We need to split the seat from the user input
    row_seat = row_seat.split()

    # We make sure the row is a number not a string
    row = int(row_seat[0])
    seat = row_seat[1]
            
    if (row,seat) in reserved_seats:
        print("That seat is taken!")

        return

    # We check if the requested row is a higher 
    # number than the row_list (total)
    # or if the char is not in the row
    if (len(row_list) < row or seat not in row_list[row-1]):
        print("Seat number is invalid!")

        return

    for i in range(0,len(row_list)):

        # Check if the current row is the requested row
        if i == row-1:

            # Find the seat number in the requested row
            for x in range(0,len(row_list[i])):
                
                # If the current seat matches the requested seat
                # we replace the char with "X" and update the
                # reserved_seats list 
                if row_list[i][x] == seat:
                    row_list[i][x] = "X"
                    reserved_seats.append((row,seat))

    return True

def reserving_seats(row_list, reserved_seats):
    '''Ask the user for the seat number, 
        prints out an updated plane list if seat available'''

    row_seat = input("Input seat number (row seat): ")

    reserve_seat_results = reserve_seat(row_seat,row_list,reserved_seats)

    # If true we print the plane
    if reserve_seat_results:

        # Print out the current status of the plane
        print_plane(row_list)

    # If false we start with the function again
    else:
        reserving_seats(row_list, reserved_seats)

    return 
            
def more_seats(row_list, reserved_seats):
    '''Allows the user to reserve more than one seat'''
    while True:
        more_seats = input("More seats (y/n)? ")
        if more_seats == "y":
            
            reserving_seats(row_list, reserved_seats)

        elif more_seats == 'n':
            break

    return row_list, reserved_seats

def main():

    rows = get_number_of_rows()
    seats = get_number_of_seats()
    
    # set up the list
    row_list = data_list(rows,seats)

    # print out the plane
    print_plane(row_list)
    
    reserved_seats = []

    # start reserving seats
    reserving_seats(row_list,reserved_seats)

    # reserve more seats
    more_seats(row_list,reserved_seats)


main()