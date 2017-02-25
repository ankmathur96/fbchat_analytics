import fbchat
import consts
import time
import pickle
import sys
import signal
import sys
TOTAL_LIM = 50000
LIMIT = 1000
CHAT_ID = '100000054197818'
BRO_CHAT_ID = '1430596130300043'
IS_GROUP = True
CHAT_ID = BRO_CHAT_ID
output_fname = sys.argv[1]
def output_obj(obj):
	obj = obj[::-1]
	with open(output_fname, 'w') as out_f:
		pickle.dump(obj, out_f)

c = fbchat.Client(consts.username, consts.password)
all_messages = []
last_ts = None
starting_offset = 0
offset = starting_offset
initializing = True
def signal_handler(signal, frame):
        print('You pressed Ctrl+C! Saving messages...')
        output_obj(all_messages)
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
while initializing or len(messages) > 1 or len(all_messages) > TOTAL_LIM:
	initializing = False
	messages = c.getThreadInfo(CHAT_ID, offset, LIMIT, last_ts, is_group=IS_GROUP)
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
	offset += LIMIT
output_obj(all_messages)
