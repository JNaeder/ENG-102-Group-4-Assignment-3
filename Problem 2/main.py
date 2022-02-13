#Assignment 3 Problem 2: Positive/Negative Predictive Values

#Data set: 50 tuples of (bool, bool) representing (positive, accurate),
# i.e. (True, True) is a true positive, (False, True) is a true negative,
# (True, False) is a false positive, and (False, False) is a false negative.
diagnoses = [(True, True), (True, True), (True, False), (True, False), 
			(False, True), (True, False), (False, True), (False, False), 
			(True, True), (False, True), (False, False), (False, False), 
			(False, False), (True, True), (False, False), (True, True), 
			(True, False), (False, False), (False, True), (False, True), 
			(True, True), (True, True), (False, True), (False, True), 
			(False, True), (True, False), (False, False), (False, False), 
			(False, True), (False, True), (False, True), (True, False), 
			(True, False), (True, False), (True, True), (False, True), 
			(True, False), (True, False), (True, False), (False, False), 
			(False, True), (False, True), (True, True), (True, False), 
			(True, False), (True, True), (False, False), (False, True), 
			(False, False), (False, False)]

def count_positives(test_results):
	"""
	Returns the number of (true and false) positive results in test_results.
	Do not change this function.
	"""
	return sum([1 for tup in test_results if tup[0] == True])

def count_negatives(test_results):
	"""
	Returns the number of (True and false) negative results in test_results.
	Do not change this function.
	"""
	return sum([1 for tup in test_results if tup[0] == False])

def count_accurate(result_type, test_results):
	"""
	Returns the number of True result_type results in test_results,
	 e.g. count_accurate(True, diagnoses) 
	 would return the number of True positives in diagnoses, and
	 count_accurate(False, diagnoses) would return the True negatives.
	Do not change this function.
	"""
	return(sum([1 for tup in test_results if tup[0] == result_type and tup[1] == True]))

def count_inaccurate(result_type, test_results):
	"""
	Returns the number of inaccurate results in test_results,
	 e.g. count_inaccurate(True, diagnoses)
	 would return the number of False positives in diagnoses.
	Do not change this function.
	"""
	return(sum([1 for tup in test_results if tup[0] == result_type and tup[1] == False]))

def count_tests(test_results):
	"""
	Returns the total number of results in test_results.
	Do not change this function.
	"""
	return len(test_results)

#########################################
#Complete the following two functions.	#
#You may call the functions above,		#
# but do not define any new functions.	#
#You will need to add parameters.		#
#You may also use arithmetic operators, #
# i.e. +, -, *, **, /					#
#########################################
def calc_pos_pred_value(result_type, test_results):
    positives = count_positives(test_results)
    accurate = count_accurate(result_type, test_results)
    pos_pred = accurate / positives
    return pos_pred

def calc_neg_pred_value(result_type, test_results):
    negatives = count_negatives(test_results)
    inaccurate = count_inaccurate(result_type, test_results)
    neg_pred = inaccurate / negatives
    return neg_pred

# Call calc_pos_pred_value() and calc_neg_pred_value() with the necessary arguments.
# The necessary arguments should be values returned from other functions, 
#   based on the tuple(test cases) of diagnoses.
positive_predictive_value = calc_pos_pred_value(True, diagnoses)
negative_predictive_value = calc_neg_pred_value(False, diagnoses)