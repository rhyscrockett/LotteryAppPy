def findwinningnumbers(genticket, dataset):
    matchingnumbers = []                                 # list to hold items that appear in both tickets
    totalmatchingnumbers = []                            # list that holds the number of total winning numbers (i.e. any number with 1 or more matching numbers)
    print("SHOULD BE EMPTY LITS: ", matchingnumbers)
    print("SHOULD BE EMPTY LISTS: ", totalmatchingnumbers)
    for ticket in dataset:                                  # for each row (ticket) in the dataset
        #print(row)                                      # prints the individual rows (7 numbers of ticket)
        for number in ticket:                               # for each item in the row
            #print(item)                                 # prints the individual items (numbers of ticket)
            if int(number) in genticket:                 # check if the number is in generated ticket
                matchingnumbers.append(number)           # add the count number to the matching numbers list
                #print(f"Matching number found: {number}")# print the count of matching numbers
            else:
                continue                                 # continue to the next number in the ticket
        #print(matchingnumbers)
            
        if matchingnumbers:                               # if there is matching numbers in matchingnumbers
            count = len(matchingnumbers)                  # use the length of matchingnumbers list to store the count of winning numbers on ticket
            #print(f"(Row Counter: {count})\n")             # print the count for that ticket
            totalmatchingnumbers.append(count)            # add the numbers found for that ticket to another list
        matchingnumbers.clear()                      # clear the matchingnumbers list for the next ticket

    print(totalmatchingnumbers)
    total = len(totalmatchingnumbers)
    print("-----------------------------------")
    print("1 matching number:", totalmatchingnumbers.count(1))
    print("2 matching numbers:", totalmatchingnumbers.count(2))
    print("3 matching numbers:", totalmatchingnumbers.count(3))
    print("4 matching numbers:", totalmatchingnumbers.count(4))
    print("5 matching numbers:", totalmatchingnumbers.count(5))
    print("6 matching numbers:", totalmatchingnumbers.count(6))
    print("7 matching numbers:", totalmatchingnumbers.count(7))
    print("\nTotal Matching Numbers: ", total)            # print statement      
    print("-----------------------------------")
    totalmatchingnumbers.clear()
    print("EMPYTY LIST BEFORE ENDING PROGRAM: ", totalmatchingnumbers)
