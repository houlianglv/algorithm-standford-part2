# This problem also asks you to solve a knapsack instance, but a much bigger one.
# Download the text file here. This file describes a knapsack instance, and it has the following format:
# [knapsack_size][number_of_items] #2000000 2000
# [value_1] [weight_1]
# [value_2] [weight_2]
# ...
# For example, the third line of the file is "50074 834558", indicating that the second item has value 50074 and size 834558, respectively. As before, you should assume that item weights and the knapsack capacity are integers.

# This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space. So you will have to be creative to compute an optimal solution. One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.

# In the box below, type in the value of the optimal solution.

# ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
# the answer for this question is 4243395
import pandas as pd


def load_data():
    """load data from file"""
    data = pd.read_csv("knapsack_big.txt", header=0, sep=' ')
    return data

def knapspack(data):
    """another implementation"""
    pre = []
    pair = [0, 0]
    pre.append(pair)
    for index, item in data.iterrows():
        new_row = generate_new_row(pre, item)
        pre = new_row
    return new_row[-1][-1]

def generate_new_row(pre, item):
    """generate new row with current item and pre row"""
    new_row = []
    temp_row = []
    for pair in pre:
        temp_row.append([pair[0] + item["weight"], pair[1] + item["value"]])
    pre_index = 1
    temp_index = 0
    new_row.append([0, 0])
    while pre_index < len(pre) and temp_index < len(temp_row):
        pre_pair = pre[pre_index]
        temp_pair = temp_row[temp_index]
        if pre_pair[0] < temp_pair[0]:
            win_pair = pre_pair
            pre_index = pre_index + 1
        elif pre_pair[0] > temp_pair[0]:
            win_pair = temp_pair
            temp_index = temp_index + 1
        elif pre_pair[1] > temp_pair[1]:
            win_pair = pre_pair
            pre_index = pre_index + 1
        else:
            win_pair = temp_pair
            temp_index = temp_index + 1
        add_new_item(win_pair, new_row)
    while pre_index < len(pre):
        add_new_item(pre[pre_index], new_row)
        pre_index = pre_index + 1
    while temp_index < len(temp_row):
        add_new_item(temp_row[temp_index], new_row)
        temp_index = temp_index + 1
    return new_row

def add_new_item(win_pair, new_row):
    """add win pair to the new row"""
    if win_pair[0] > 2000000:
        return
    last_add_pair = new_row[-1]
    if win_pair[0] > last_add_pair[0] and win_pair[1] > last_add_pair[1]:
        new_row.append(win_pair)
    elif win_pair[0] == last_add_pair[0] and win_pair[1] > last_add_pair[1]:
        new_row.pop()
        new_row.append(win_pair)
