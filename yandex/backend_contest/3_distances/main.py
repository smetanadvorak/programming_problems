import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
with open(inputname, 'r') as f:
    n, k = tuple(map(int, f.readline().split()))
    a = list(map(int, f.readline().split()))


def solution(a):
    # Strategy: to avoid exhaustive search over all combinations,
    # sort the array to have, for each element, its closest
    # elements (in terms of |a_i - a_j|) next to it.

    # Remember the original order to reorder the output. Sort the array.
    sorted_indices  = sorted(range(len(a)), key=a.__getitem__)
    reverse_indices = sorted(range(len(a)), key=sorted_indices.__getitem__)
    a = [a[i] for i in sorted_indices]

    # Main loop
    result = [0 for i in a] # To store minimal distances
    for i in range(len(a)):
        dist = 0 # Accumulator of distances
        left, right = i-1, i+1 # Left and right neighbours of the i-th element
        for neighbour in range(k):
            # If on either of the edges of the array, only one neighbour is possible:
            if left == -1:
                dist += abs(a[i] - a[right])
                right += 1
            elif right == len(a):
                dist += abs(a[i] - a[left])
                left -= 1
            # Otherwise, always take the closest neighbour into the distance calculation.
            else:
                dist_right = abs(a[i] - a[right])
                dist_left  = abs(a[i] - a[left ])
                dist += min(dist_left, dist_right)
                if dist_right < dist_left:
                    right += 1
                else:
                    left -= 1
        result[reverse_indices[i]] = dist
    return result#[result[i] for i in reverse_indices]



# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(' '.join(map(str, solution(a)))+'\n')
