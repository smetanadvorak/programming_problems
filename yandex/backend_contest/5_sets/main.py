# Назовём неориентированный граф простым, если в нём нет петель и кратных рёбер. Назовём простой неориентированный граф хорошим, если в нём ровно у одной вершины степень равна , то есть в графе есть ровно одна вершина, соединённая со всеми остальными ребром.
# Дано число n, требуется посчитать количество хороших графов на n вершинах. Два графа называются различными, если существует пара вершин  такая, что в одном графе есть ребро , а в другом нет.
# Так как ответ может быть крайне большим, выведите отстаток от его деления на 10^9 + 7.


import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

allowed = {'diag':['=', '>', '<', '?'], ''}

# Read input
with open(inputname, 'r') as f:
    n = int(f.readline())
    table = []
    for i in range(n):
        table.append(f.readline())

def solution(n):
    # Check for fatal inconsistencies
    # 1) Diagonal elements (either =, >, < or ?)
    #

# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(str(solution(n))+'\n')
