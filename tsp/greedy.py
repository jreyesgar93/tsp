import copy


def greedy():
	start=np.random.choice(MAX_CITIES)
	current=start
	path=[start]
	cost=0.0

	local_distances=copy.deepcopy(distances)

	while len(path) < MAXCITIES:
		distances_to=no.copy(local_distnces[current,:])
		distances_to[path]=np.infty
	
		current = np.argmin(distances_to)
		path.append(current)
		cost+=np.min(distances_to)
		print(path,cost,current)
	
	return cost, path	
