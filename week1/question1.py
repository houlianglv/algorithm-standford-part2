# The answer is 69119377652
# In this programming problem and the next
# you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times..
# Download the text file jobs.txt.
# (I modifed the file by adding header in the first line to make it easier for performing pandas operation)
# This file describes a set of jobs with positive and integral weights and lengths. It has the format
# [number_of_jobs]
# [job_1_weight] [job_1_length]
# [job_2_weight] [job_2_length]
# ...
# For example, the third line of the file is "74 59",
# indicating that the second job has weight 74 and length 59.
# You should NOT assume that edge weights or lengths are distinct.

# Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order
# of the difference (weight - length). Recall from lecture that this algorithm is not always optimal.
# IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first.
# Beware: if you break ties in a different way, you are likely to get the wrong answer.
# You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
import pandas as pd

def preprocessData():
    df = pd.read_csv('jobs.txt', sep=' ', header=0)
    df['diff'] = df['weight'] - df['length']
    res = df.sort(['diff', 'weight'], ascending=[0, 0])
    return res

def calculateWl(data):
    #data is the result of preprocessData()
    #wl means weight*completeTime
    data['wl'] = 0
    sumTime = 0
    for row in data.iterrows():
        sumTime += row[1]['length']
        row[1]['wl'] = sumTime*row[1]['weight']
    return sum(data['wl'])

