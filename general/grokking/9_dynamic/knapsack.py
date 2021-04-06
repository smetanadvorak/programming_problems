items = {}
items['water'] = {'weight': 3, 'value' : 10}
items['book'] = {'weight': 1, 'value' : 3}
items['food'] = {'weight': 2, 'value' : 9}
items['jacket'] = {'weight': 2, 'value' : 5}
items['camera'] = {'weight': 1, 'value' : 6}

volume = 6
step = 1

def fill_knapsack_value(volume, weight, value):
	assert(len(weight) == len(value))

	valuetab = [[0] * (volume+1) for _ in range(len(weight)+1)]
	for i in range(len(valuetab)):
		for w in range(len(valuetab[0])):
			if i==0 or w==0:
				valuetab[i][w] = 0
			elif weight[i-1] <= w:
				valuetab[i][w] = max(valuetab[i-1][w], value[i-1] + valuetab[i-1][w - weight[i-1]])
			else:
				valuetab[i][w] = valuetab[i-1][w]
	return valuetab

def fill_knapsack_list(items, volume):
	weights = range(1, volume + 1, step)
	valuetab = [ [0]*(volume+1) for _ in range(len(items)+1)]
	itemstab = [ ['']*(volume+1) for _ in range(len(items)+1)]

	i = 1
	j = 1
	for item in items:
		for weight in weights:
			if (weight >= items[item]['weight']):
				if items[item]['value'] + valuetab[i-1][weight - items[item]['weight']] > valuetab[i-1][j]:
					valuetab[i][j] = items[item]['value'] + valuetab[i-1][weight - items[item]['weight']]
					itemstab[i][j] = itemstab[i-1][weight - items[item]['weight']] + '+' + item
				else:
					valuetab[i][j] = valuetab[i-1][j]
					itemstab[i][j] = itemstab[i-1][j]
			else:
				valuetab[i][j] = valuetab[i-1][j]
			j = j + 1
		i = i + 1
		j = 1
	return valuetab, itemstab

# values, things_to_take = fill_knapsack_list(items, volume, step)
# for i in range(len(values)):
# 	print(values[i])
# 	print(things_to_take[i])

valuetab = fill_knapsack_value(volume, [item['weight'] for item in items.values()], [item['value'] for item in items.values()])
print(valuetab)
