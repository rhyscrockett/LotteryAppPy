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

    return totalmatchingnumbers

def save_winning_numbers(matchingnumbers, ticket):
    total = len(matchingnumbers)
    ticket = str(ticket)
    with open("results.txt", "a") as f:
        f.write("-----------------------------------")
        f.write(f"\nTicket: {ticket}")
        f.write(f"\n1 matching number: {matchingnumbers.count(1)}")
        f.write(f"\n2 matching numbers: {matchingnumbers.count(2)}")
        f.write(f"\n3 matching numbers: {matchingnumbers.count(3)}")
        f.write(f"\n4 matching numbers: {matchingnumbers.count(4)}")
        f.write(f"\n5 matching numbers: {matchingnumbers.count(5)}")
        f.write(f"\n6 matching numbers: {matchingnumbers.count(6)}")
        f.write(f"\n7 matching numbers: {matchingnumbers.count(7)}")
        f.write(f"\nTotal matching Numbers from Dataset: {total}")
        f.write("\n-----------------------------------\n\n")
