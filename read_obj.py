import sys
import pickle
import datetime
import json

filename = sys.argv[1]

with open(filename, 'r') as in_file:
	m = pickle.load(in_file)
