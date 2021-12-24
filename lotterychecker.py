def findwinningnumbers(genticket, winningticket):
    matchingnumbers = []
    for i in genticket:
        if i in winningticket:
            matchingnumbers.append(i)
    return matchingnumbers
