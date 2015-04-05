# The answer is 67311454237
# For this problem, use the same data set as in the previous problem. 
# Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order 
# of the ratio (weight/length). In this algorithm, it does not matter how you break ties. 
# You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
import pandas as pd

def preprocessData():
	df = pd.read_csv('jobs.txt', sep=' ', header=0)
	df['ratio'] = df['weight'] / df['length']
	res = df.sort(['ratio', 'weight'], ascending=[0, 0])
	return res

def calculateWl(data):
	#data is the result of preprocessData()
	#wl means weight*completeTime
	data['wl'] = 0
	sumTime = 0
	sumWl = 0
	for row in data.iterrows():
		sumTime += row[1]['length']
		row[1]['wl'] = sumTime*row[1]['weight']
		print row[1]['wl']
		sumWl += row[1]['wl']
	return sumWl