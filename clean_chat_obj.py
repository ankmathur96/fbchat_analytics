import pickle
import sys
fname = sys.argv[1]
messages = []
with open(fname, 'r') as in_file:
	messages = pickle.load(in_file)
	sorted_messages = sorted(messages, key=lambda x: int(x.timestamp))
	cleaned = []
	i = 0
	while i < len(sorted_messages):
		try:
			if sorted_messages[i-1].body != sorted_messages[i].body:
				cleaned.append(sorted_messages[i])
		except:
			cleaned.append(sorted_messages[i])
		i += 1
	print(len(cleaned))
	print(len(messages))
	with open(fname.split('.')[0] + '_cleaned' + '.pk', 'w') as out_file:
		pickle.dump(cleaned, out_file)

