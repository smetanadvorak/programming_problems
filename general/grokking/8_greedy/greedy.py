states_needed = {'mt','wa','or','id','nv','ut','ca','az'}
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca','az'])


def greedy(states_needed, stations):
	final_covered = set([])
	final_stations = []
	while len(states_needed) > 0:
		# Find the best station
		best_covered = 0
		best_station = None
		for s in stations:
			if len(stations[s] & states_needed) > best_covered:
				best_covered = len(stations[s] & states_needed)
				best_station = s
				
		if best_covered:
			final_stations.append(best_station)	
			final_covered = final_covered.union(stations[best_station])
			states_needed = states_needed.difference(stations[best_station])
		else: 
			break
		
	return final_covered, final_stations
	

print(greedy(states_needed, stations))
print(states_needed)