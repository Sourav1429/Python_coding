def load_doc(filename):
	# open the file as read only
	file = open(filename, mode='rt', encoding='utf-8')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
path='C://Users//Debasis//Documents//legend.txt'
text=load_doc(path)
