def findwinningnumbers(genticket, dataset):
    matchingnumbers = []
    count = 0
    for row in dataset:                               # for each row (ticket) in the dataset
        #print(row)                                   # prints the individual rows (7 numbers of ticket)
        for item in row:                              # for each item in the row
            #print(item)                              # prints the individual items (numbers of ticket)
            if int(item) in genticket:                # check if the item (number: converted to int) is in generated ticket
                matchingnumbers.append(item)          # if true, add to the matchingnumbers array
                count = len(matchingnumbers)          # set count to the length of the array (counts how many numbers match)
    print(f"Matching numbers: {count}")
    return matchingnumbers
    #return count
