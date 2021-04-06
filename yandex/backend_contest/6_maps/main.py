import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
shots = []
with open(inputname, 'r') as f:
    n = int(f.readline())
    for i in range(n):
        shots.append(list(map(int, f.readline().split())))

def area(rect):
    res = abs((rect[2]-rect[0]) * (rect[3]-rect[1]))
    print((rect[2]-rect[0]), (rect[3]-rect[1]))
    return -res if any([rect[2]-rect[0] < 0, rect[3]-rect[1] < 0]) else res

def find_intersection(rectangles):
    xs = sorted([r[0] for r in rectangles] + [r[2] for r in rectangles])
    ys = sorted([r[1] for r in rectangles] + [r[3] for r in rectangles])
    print([xs[len(rectangles)-1], xs[len(rectangles)], ys[len(rectangles)-1], ys[len(rectangles)]])
    return [xs[len(rectangles)-1], xs[len(rectangles)], ys[len(rectangles)-1], ys[len(rectangles)]]

def check_intersection(rect1, rect2):
    return max(area(find_intersection([rect1, rect2])), 0)

print(check_intersection([-1,-1, 1, 1], [-5,2,-4,3]))

# Solution here:
def solution(shots):
    result = [0] * len(shots)
    for (i, shot) in enumerate(shots):
        current_shot = [shot.copy()]
        result[i]  = area(shot)
        for (j, newer_shot) in enumerate(shots[i:]):
            intersection = find_intersection([current_shot[0], newer_shot])
            result[i]
            current_shot.append(intersection)


# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(str(solution(shots))+'\n')


# OK
# # Read input
# with open('input.txt', 'r') as f:
#     n = int(f.readline())
#     a = list(map(int, f.readline().split()))
#
#
# def solution(a):
#     if len(a) == 1:
#         return 0
# 	# If the list is decreasing somewhere, impossible to equalize volumes
#     if any([a[i-1]>a[i] for i in range(1, len(a))]):
#         return -1
#     return a[-1] - a[0] #Takes this much to equalize volumes
#
# with open('output.txt', 'w') as f:
# 	f.write(str(solution(a)))
