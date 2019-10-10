
# 1 Taka inn input frá notanda, rows og seats
# 2 prenta raðir og sæti með 2ja stafa breidd fyrir númer raða og 3 bil eftir það, 3 bil er gangurinn,
# og eitt bil á milli sæta
# Einn gangur,fjöldi sæta í röð er slétt tala >=2
# 3 fá input frá notanda með sætinr, Taka frá sæti, if input er ákveðið þá setjum við X í staðinn. 
# 4

SEATS = [A,B,C,D,E,F,G,H,I,J]

def get_number_of_rows():
    ''' returns a number of rows '''
    rows = input("Enter number of rows: ")

    return rows

def get_number_of_seats():
    ''' returns a number of seats '''
    seats = input("Enter number of seats in each row: ")

    return seats

def data_list():
    pass




def main():


    while True:
        more_seats = input("More seats (y/n)? ")

        if more_seats == "y":
            input("Input seat number (row seat): ")
                # ef sæti er tekið
                    print("That seat is taken!")
                # ef sæti er ekki til
                    print("Seat number is invalid!")

    else:
        break