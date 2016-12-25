import fbchat
import consts
import time
import pickle
import sys
from read_obj import load_file

LIMIT = 80
CHAT_ID = '100000054197818'
prev_messages = sys.argv[1]
output_fname = sys.argv[2]
def output_obj(obj):
	with open(output_fname, 'w') as out_f:
		pickle.dump(obj, out_f)

prev_m = load_file(prev_messages)
c = fbchat.Client(consts.username, consts.password)
all_messages = []
last_ts = None
ts_end = int(prev_m[-1].timestamp)
starting_offset = 0
initializing = True
while last_ts > ts_end and ((not initializing and len(messages) > 1) or initializing):
	initializing = False
	messages = c.getThreadInfo(CHAT_ID, offset, LIMIT, last_ts)
	# new to old sorted, so we reverse it.
	messages = sorted(messages, key=lambda x: int(x.timestamp))[::-1]
	last_ts = int(messages[-1].timestamp)
	print(len(messages))
	time.sleep(1)
	if messages is None:
		output_obj(all_messages)
		raise Exception('request failed ' + str(offset))
	# for m in messages:
	# 	print(m.timestamp)
	all_messages.extend(messages)
	starting_offset += LIMIT
all_messages = all_messages[::-1]
output_obj(prev_m + all_messages)
