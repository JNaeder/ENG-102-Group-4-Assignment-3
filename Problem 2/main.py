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

def calc_pos_pred_value(result_type, test_results):
    """
	Returns positive predicitive value given the True result type and the data set as input.
	"""
    positives = count_positives(test_results)
    accurate = count_accurate(result_type, test_results)
    pos_pred = accurate / positives
    return pos_pred

def calc_neg_pred_value(result_type, test_results):
    """
	Returns negative predicitive value given the True result type and the data set as input.
	"""
    negatives = count_negatives(test_results)
    accurate = count_accurate(result_type, test_results)
    neg_pred = accurate / negatives
    return neg_pred


# TEST CASES

print("\n----------Test Data 1----------")
test_data_1 = [(True, True),(True, False),(False, True),(False, False)]
print("Expected Positive Predictive Output = 0.5: Actual Output = " + str(calc_pos_pred_value(True, test_data_1))) #Expected output = 0.5
print("Expected Negative Predictive Output = 0.5: Actual Output = " + str(calc_neg_pred_value(False, test_data_1))) #Expected output = 0.5

print("\n----------Test Data 2----------")
test_data_2 = [(True, True),(True, True),(False, True),(False, True)]
print("Expected Positive Predictive Output = 1: Actual Output = " + str(calc_pos_pred_value(True, test_data_2))) #Expected output = 1
print("Expected Negative Predictive Output = 1: Actual Output = " + str(calc_neg_pred_value(False, test_data_2))) #Expected output = 1

print("\n----------Test Data 3----------")
test_data_3 = [(True, False),(True, False),(False, False),(False, False)]
print("Expected Positive Predictive Output = 0: Actual Output = " + str(calc_pos_pred_value(True, test_data_3))) #Expected output = 0
print("Expected Negative Predictive Output = 0: Actual Output = " + str(calc_neg_pred_value(False, test_data_3))) #Expected output = 0

print("\n----------Test Data 4----------")
test_data_4 =   [(True, True),(True, True),(True, True),(True, False),(False, True),(False, True),(False, True),
				(False, False),(True, True),(True, True),(True, True),(True, False),(False, True),(False, True),
				(False, True),(False, False),(True, True),(True, True),(True, True),(True, False),(False, True),
				(False, True),(False, False),(False, False),(True, True),(True, True),(True, True),(True, False),
				(False, False),(False, False),(False, False),(False, False)]
print("Expected Positive Predictive Output = 0.75: Actual Output = " + str(calc_pos_pred_value(True, test_data_4))) #Expected output = 0.75
print("Expected Negative Predictive Output = 0.5: Actual Output = " + str(calc_neg_pred_value(False, test_data_4))) #Expected output = 0.5

print("\n----------Real Data----------")
positive_predictive_value = calc_pos_pred_value(True, diagnoses)
negative_predictive_value = calc_neg_pred_value(False, diagnoses)
print("Positive Predictive Value = " + str(positive_predictive_value))
print("Negative Predictive Value = " + str(negative_predictive_value))
print("")
