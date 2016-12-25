import sys
import pickle

filename = sys.argv[1]

def load_file(fname):
	with open(filename, 'r') as in_file:
		m = pickle.load(in_file)
		return m

if __name__ == '__main__':
	filename = sys.argv[1]
	m = load_file(filename)