def findwinningnumbers(genticket, dataset):
    matchingnumbers = []
    count = 0
    for row in dataset:                               # for each row (ticket) in the dataset
        print(row)                                    # prints the individual rows (7 numbers of ticket)
        for item in row:                              # for each item in the row
            #print(item)                              # prints the individual items (numbers of ticket)
            if int(item) in genticket:                # check if the item (number: converted to int) is in generated ticket
                count += 1                            # increase the counter by 1
                print(f"Matching numbers: {count}")   # print the count of matching numbers
                matchingnumbers.append(count)         # add the count number to the matching numbers list
            else:
                count = 0
                continue
            #count = 0

    return len(matchingnumbers)                       # return the length (numbers of) the array
