import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Seat column-letter dictionary
seat_columns = {0:'A', 1:'B', 2:'C', 4:'D', 5:'E', 6:'F'}

# Solution here:
def solution(occupation, sz, side, whim):
    if side == 'left':
        required_seat  = 0 if whim == 'window' else  2
        fill_direction = 1 if whim == 'window' else -1
    else:
        required_seat  =  6 if whim == 'window' else 4
        fill_direction = -1 if whim == 'window' else 1

    for (i,row) in enumerate(occupation):
        occupation_possible = True
        for passenger in range(sz):
            if row[required_seat + passenger * fill_direction] == '#': # If the seat is taken
                occupation_possible = False
                break # Stop trying to place the group in this row

        if occupation_possible:
            # Print result
            print('Passengers can take seats:', end='')
            for passenger in range(sz) if fill_direction == 1 else reversed(range(sz)):
                print(' %d%s' % (i+1, seat_columns[required_seat + passenger * fill_direction]), end='')
            print()

            # Show new occupation
            for passenger in range(sz):
                row[required_seat + passenger * fill_direction] = 'X'

            # Print new occupation
            [print(''.join(row)) for row in occupation]

            # Update the occupation with #
            for passenger in range(sz):
                row[required_seat + passenger * fill_direction] = '#'

            return # Stop the search across rows and exit

    print('Cannot fulfill passengers requirements')
    return


# Read input
occupation = []
with open(inputname, 'r') as f:
    n = int(f.readline()) # Number of rows
    for row in range(n):
        occupation.append(list(f.readline()[:-1]))

    m = int(f.readline()) # Number of groups
    for group in range(m):
        sz, side, whim = tuple(f.readline().split())
        solution(occupation, int(sz), side, whim)
