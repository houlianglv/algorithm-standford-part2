# In this programming problem and the next you'll code up the knapsack algorithm from lecture. Let's start with a warm-up. Download the text file here. This file describes a knapsack instance, and it has the following format:
# [knapsack_size][number_of_items]  #10000 100
# [value_1] [weight_1]
# [value_2] [weight_2]
# ...
# For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.
# You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

# In the box below, type in the value of the optimal solution.

# ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
# the answer for this question is 2493893
import pandas as pd
import numpy as np

def load_data():
    """load data from file"""
    data = pd.read_csv("knapsack1.txt", header=0, sep=' ')
    return data

def max_value(darray, i, weight, row):
    """retrive the maximum value in sub-problem"""
    if weight < row["weight"]:
        return darray[i-1, weight]
    elif darray[i-1, weight] > darray[i-1, weight-row["weight"]]+row["value"]:
        return darray[i-1, weight]
    else:
        return darray[i-1, weight-row["weight"]]+row["value"]

def knapspack(data):
    """do knapspack algorithm"""
    darray = np.zeros(shape=(101,10001), dtype=np.int64)
    for i, row in data.iterrows():
        for weight in range(10001):
            darray[i+1, weight] = max_value(darray, i+1, weight, row)
    return darray[100, 10000]
