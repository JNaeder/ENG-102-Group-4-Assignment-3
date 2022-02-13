# Assignment 3 Problem 1: Z-score

# Data set: a list of integers
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

def z_score(data_point, data_set):
    mean_of_set = mean(data_set)
    standard_deviation = stdev(data_set, mean_of_set)
    zscore = (data_point - mean_of_set) / standard_deviation
    return zscore


# TEST CASES

print("\n----------Test 1----------")
test_data_1 = [2, 4]
print("Expected Mean Output = 0 : Actual Mean Output = " + str(z_score(mean(test_data_1), test_data_1)))
print("Expected Greatest Output = 1.0 : Actual Greatest Output = " + str(z_score(greatest(test_data_1), test_data_1)))
print("Expected Least Output = -1.0 : Actual Least Output = " + str(z_score(least(test_data_1), test_data_1)))

print("\n----------Test 2----------")
test_data_2 = [6, 7, 7, 12, 13, 13, 15, 16, 19, 22]
print("Expected Mean Output = 0 : Actual Mean Output = " + str(z_score(mean(test_data_2), test_data_2)))
print("Expected Greatest Output = 1.79 : Actual Greatest Output = " + str(z_score(greatest(test_data_2), test_data_2)))
print("Expected Least Output = -1.39 : Actual Least Output = " + str(z_score(least(test_data_2), test_data_2)))

print("\n----------Test 3----------")
test_data_3 = [5, 6, 7, 7, 8]
print("Expected Mean Output = 0 : Actual Mean Output = " + str(z_score(mean(test_data_3), test_data_3)))
print("Expected Greatest Output = 1.37 : Actual Greatest Output = " + str(z_score(greatest(test_data_3), test_data_3)))
print("Expected Least Output = -1.57 : Actual Least Output = " + str(z_score(least(test_data_3), test_data_3)))

print("\n----------Test 4----------")
test_data_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Expected Mean Output = 0 : Actual Mean Output = " + str(z_score(mean(test_data_4), test_data_4)))
print("Expected Greatest Output = 1.65 : Actual Greatest Output = " + str(z_score(greatest(test_data_4), test_data_4)))
print("Expected Least Output = -1.65 : Actual Least Output = " + str(z_score(least(test_data_4), test_data_4)))

print("\n----------Real Data----------")
mean_z_score = z_score(mean(population), population)
greatest_z_score = z_score(greatest(population), population)
least_z_score = z_score(least(population), population)
print("Mean Z-Score = " + str(mean_z_score))
print("Greatest Z-Score = " + str(greatest_z_score))
print("Least Z-Score = " + str(least_z_score))
print("")
