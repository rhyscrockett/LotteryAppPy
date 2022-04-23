def find_winning_numbers(genticket, dataset):
    matchingnumbers = [] # list to hold items that appear in both tickets
    totalmatchingnumbers = [] # list that holds the number of total winning numbers (i.e. any number with 1 or more matching numbers)
    for row in dataset:                                  # for each row (ticket) in the dataset
        #print(row)                                      # prints the individual rows (7 numbers of ticket)
        for number in row:                               # for each item in the row
            #print(item)                                 # prints the individual items (numbers of ticket)
            if int(number) in genticket:                 # check if the number is in generated ticket
                matchingnumbers.append(number)           # add the count number to the matching numbers list
                #print(f"Matching number found: {item}") # print the count of matching numbers
            else:
                continue                                 # continue to the next number in the ticket
            
        for x in matchingnumbers:                        # if there is matching numbers in matchingnumbers
            count = len(matchingnumbers)                 # use the length of matchingnumbers list to store the count
            #print(f"\t(Counter: {count})\n")            # print the count for that ticket
            totalmatchingnumbers.append(count)           # add the numbers found for that ticket to another list
            # totalmatchingnumbers returns matching numbers for each ticket
            matchingnumbers.clear()                      # clear the matchingnumbers list for the next ticket

    total = len(totalmatchingnumbers)
    print("-----------------------------------")
    print("1 matching number:", totalmatchingnumbers.count(1))
    print("2 matching numbers:", totalmatchingnumbers.count(2))
    print("3 matching numbers:", totalmatchingnumbers.count(3))
    print("4 matching numbers:", totalmatchingnumbers.count(4))
    print("5 matching numbers:", totalmatchingnumbers.count(5))
    print("6 matching numbers:", totalmatchingnumbers.count(6))
    print("7 matching numbers:", totalmatchingnumbers.count(7))
    print("\nTotal Matching Numbers from Dataset:", total)            # print statement
    print("-----------------------------------")

