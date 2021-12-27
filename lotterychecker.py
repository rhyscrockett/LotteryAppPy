def findwinningnumbers(genticket, winningticket):
    matchingnumbers = []
    for row in winningticket:
        print(row)                                   # prints the individual rows (7 numbers of ticket)
        for item in row:
            print(item)                              # prints the individual items (numbers of ticket)
            if item in genticket:
                matchingnumbers.append(item)
    return matchingnumbers
