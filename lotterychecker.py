def findwinningnumbers(genticket, dataset):
    matchingnumbers = []                                # list to hold items that appear in both tickets
    totalmatchingnumbers = []                           # list that holds the number of total winning numbers
    count = 0                                           # count variable holds the counter value
    for row in dataset:                                 # for each row (ticket) in the dataset
        print(row)                                      # prints the individual rows (7 numbers of ticket)
        for item in row:                                # for each item in the row
            #print(item)                                # prints the individual items (numbers of ticket)
            if int(item) in genticket:                  # check if the item (number: converted to int) is in generated ticket
                matchingnumbers.append(item)            # add the count number to the matching numbers list
                print(f"Matching number found: {item}") # print the count of matching numbers
            else:
                continue                                # if the number is not found, continue to the next number
            
        if matchingnumbers:                             # if there is matching numbers in matchingnumbers
            count = len(matchingnumbers)                # use the length of matchingnumbers list to store the count
            print(f"\t(Counter: {count})\n")            # print the count for that ticket
            totalmatchingnumbers.append(count)          # add the numbers found for that ticket to another list
            #totalmatchingnumbers.append(matchingnumbers)
            matchingnumbers.clear()                     # clear the matchingnumbers list for the next ticket
        else:                                           # if no matchingnumbers are found in list
            print("No Matching Numbers.\n")             # print statement
            continue                                    # continue to next ticket
        
    
    print("-----------------------------------")
    no1 = totalmatchingnumbers.count(1)
    print(f"Tickets with 1 matching numbers: {no1}")
    no2 = totalmatchingnumbers.count(2)
    print(f"Tickets with 2 matching numbers: {no2}")
    no3 = totalmatchingnumbers.count(3)
    print(f"Tickets with 3 matching numbers: {no3}")
    no4 = totalmatchingnumbers.count(4)
    print(f"Tickets with 4 matching numbers: {no4}")
    no5 = totalmatchingnumbers.count(5)
    print(f"Tickets with 5 matching numbers: {no5}")
    no6 = totalmatchingnumbers.count(6)
    print(f"Tickets with 6 matching numbers: {no6}")
    no7 = totalmatchingnumbers.count(7)
    print(f"Tickets with 7 matching numbers: {no7}")
    print("-----------------------------------")
    
    print("\nTotal Matching Numbers: ")                 # print statement
    return len(totalmatchingnumbers)                    # return the length (numbers of) the total dataset
    
