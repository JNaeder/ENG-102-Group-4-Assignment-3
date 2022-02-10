test_data_1 = [(True, True),(True, False),(False, True),(False, False)]
# Expected Positive Predictive Output = 0.5
# Expected Negative Predictive Output = 0.5
test_data_2 = [(True, True),(True, True),(False, True),(False, True)]
# Expected Positive Predictive Output = 1
# Expected Negative Predictive Output = 1
test_data_3 = [(True, False),(True, False),(False, False),(False, False)]
# Expected Positive Predictive Output = 0
# Expected Negative Predictive Output = 0
test_data_4 =   [(True, True),(True, True),(True, True),(True, False),(False, True),(False, True),(False, True),
				(False, False),(True, True),(True, True),(True, True),(True, False),(False, True),(False, True),
				(False, True),(False, False),(True, True),(True, True),(True, True),(True, False),(False, True),
				(False, True),(False, False),(False, False),(True, True),(True, True),(True, True),(True, False),
				(False, False),(False, False),(False, False),(False, False)]
# Expected Positive Predictive Output = 0.75
# Expected Negative Predictive Output = 0.5