import sys
import pickle

def splice(f1, f2, out_name):
	with open(f1, 'r') as in_1:
		with open(f2, 'r') as in_2:
			f1_list = pickle.load(in_1)
			f2_list = pickle.load(in_2)
			f1_list.extend(f2_list)
			with open(out_name, 'w') as out_f:
				pickle.dump(f1_list, out_f)
if __name__ == "__main__":
	f1 = sys.argv[1]
	f2 = sys.argv[2]
	out_name = sys.argv[3]
	splice(f1, f2, out_name)
	print('done.')