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
            print(f"(Counter: {count})")                # print the count for that ticket
            totalmatchingnumbers.append(matchingnumbers)# add the numbers found for that ticket to another list
            matchingnumbers.clear()                     # clear the matchingnumbers list for the next ticket
            print("\n")                                 # new line
        else:                                           # if no matchingnumbers are found in list
            print("No Matching Numbers.\n")             # print statement
            continue                                    # continue to next ticket
        
    print("\nTotal Matching Numbers: ")                 # print statement
    return len(totalmatchingnumbers)                    # return the length (numbers of) the total dataset
