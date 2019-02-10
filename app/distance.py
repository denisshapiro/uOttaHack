import math
R = 6371000 #mean radius in m

def calculate_distance(lat1, lon1, lat2, lon2):

	#Haversine's Formula

	phi1 = math.radians(lat1)
	phi2 = math.radians(lat2)
	lambda1 = math.radians(lon1)
	lambda2 = math.radians(lon2)

	delta_phi = phi2 - phi1
	delta_lambda = lambda2 - lambda1

	a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2

	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

	metres = R * c
	return metres


def shortest_distance(lat_address, lon_address, list_of_locations):
	listOfDistances = []
	shortest_distance = []
	min_index = 0
	for x in range (len(list_of_locations)):
		listOfDistances.append(calculate_distance(lat_address, lon_address, list_of_locations[x][0],list_of_locations[x][1]))
		
	index_min = min(range(len(listOfDistances)), key=listOfDistances.__getitem__)
	return list_of_locations[index_min]

# (45.4295526667286, -75.7437935927252)