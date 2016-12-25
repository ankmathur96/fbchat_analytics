import sys
import pickle

filename = sys.argv[1]
ANAGA_ID = "100000054197818"
ANKIT_ID = "100002305767744"

def load_file(fname):
	with open(filename, 'r') as in_file:
		m = pickle.load(in_file)
		return m

def print_messages(i, j, m):
	for k in range(i, j):
		author_fbid = m[k].author.split(':')[1]
		if author_fbid == ANAGA_ID:
			print("Anaga: " + str(m[k].body.encode('utf8')))
		elif author_fbid == ANKIT_ID:
			print("Ankit: " + str(m[k].body.encode('utf8')))
		else:
			print(author_fbid + ": " + str(m[k].body))

if __name__ == '__main__':
	filename = sys.argv[1]
	m = load_file(filename)