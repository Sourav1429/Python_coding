# Make a prediction with a decision tree
def predict(node, row):
	if row[node['index']] < node['value']:
		if isinstance(node['left'], dict):
			return predict(node['left'], row)
		else:
			return node['left']
	else:
		if isinstance(node['right'], dict):
			return predict(node['right'], row)
		else:
			return node['right']

dataset = [[2.771244718,1.784783929,1],
	[1.728571309,1.169761413,1],
	[3.678319846,2.81281357,1],
	[3.961043357,2.61995032,1],
	[2.999208922,2.209014212,1],
	[7.497545867,3.162953546,0],
	[9.00220326,3.339047188,0],
	[7.444542326,0.476683375,0],
	[10.12493903,3.234550982,0],
	[6.642287351,3.319983761,0]]

#  predict with a stump
stump = {'index': 0, 'right': 1, 'value': 6.642287351, 'left': 0}
for row in dataset:
	prediction = predict(stump, row)
	print('Expected=%d, Got=%d' % (row[-1], prediction))
