import random                                  # needed for the random functions

def random_ticket():
    """Generate a random set (unique) list of 7 numbers (1-50)."""
    ticket = set()                             # create an empty set 'ticket'
    for x in range(7):                         # loop through 7 times
        ticket.add(random.randint(1,50))       # add a random number between 1 and 50 to the ticket
    return ticket
