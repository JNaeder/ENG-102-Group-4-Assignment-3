#Assignment 3 Problem 1: Z-score

#Data set: a list of integers
population = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
			42, 25, 97, 49, 33, 75, 53, 14, 53, 
			45, 87, 75, 66, 62, 55, 57, 44, 44, 
			94, 19, 96, 12, 59, 86, 88, 61, 68, 
			37, 64, 19, 46, 68, 98, 19, 54, 65, 
			30, 1, 82, 76, 3]

def mean(data_set):
	"""
	This function will return the mean of the data_set(population)
	**Do not change this function**
	"""
	return sum(data_set)/len(data_set)

def stdev(data_set, avg):
	"""
	This function will return the standard deviation of the data_set(population),
	 given the mean of the data_set (avg)
	**Do not change this function**
	"""
	variance = sum([(integer - avg) ** 2 for integer in data_set])/len(data_set)
	# return the square root of the variance calculation 
	return variance ** .5
	
def least(data_set):
	"""
	returns the least value in the data_set(population)
	**Do not change this function**
	"""
	return min(data_set)
	
def greatest(data_set):
	"""
	returns the greatest value in the data_set(population)
	**Do not change this function**
	"""
	return max(data_set)

#########################################
#Complete the following function.		#
#You may call the functions above,		#
#  but do not define any others.		#
#You will need to add parameters.		#
#You may also use arithmetic operators, #
# i.e. +, -, *, **, /					#
#########################################

def z_score():
	"""
	"""
	return


# Call z_score() with necessary arguments to get the z-score for: 
# 1. the mean of the population list,
mean_z_score = z_score()
# 2. the greatest value in the population list,
greatest_z_score = z_score()
# 3. the least value in the population list.
least_z_score = z_score()
