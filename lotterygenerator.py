import random                                  # needed for the random functions

def random_ticket():
    """Generate a random set (unique) list of 7 numbers (1-50)."""
    n = list()
    for x in range(1, 51):
        n.append(x)
    ticket = random.sample(n, 7)

    return ticket
