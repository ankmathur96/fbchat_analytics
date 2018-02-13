import fbchat
import consts
import time
import pickle
import sys
import signal
import sys
TOTAL_LIMIT = 10000
LIMIT = 100
CHAT_ID = '100000054197818'
BRO_CHAT_ID = '1430596130300043'
NEW_BRO_CHAT_ID = '653213234798397'
CANTERBUDDIES_CHAT_ID = '1457902324245295'
CHAT_ID = CANTERBUDDIES_CHAT_ID

output_fname = str(sys.argv[1])

def output_obj(obj, fname, invert_order=False):
	if invert_order:
		obj = obj[::-1]
	with open(fname, 'wb') as out_f:
		pickle.dump(obj, out_f)

c = fbchat.Client(consts.username, consts.password)
all_messages, last_ts = [], None
initializing = True

def signal_handler(signal, frame):
        print('You pressed Ctrl+C! Saving messages...')
        output_obj(all_messages, fname=output_fname, invert_order=True)
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
n_batches = TOTAL_LIMIT / LIMIT
i = 0
try:
	while (initializing or len(messages) > 1) and len(all_messages) < TOTAL_LIMIT:
		initializing = False
		if last_ts is None:
			messages = c.fetchThreadMessages(CHAT_ID, LIMIT)
		else:
			# last_ts - 1 because you don't want the same message twice.
			messages = c.fetchThreadMessages(CHAT_ID, LIMIT, last_ts-1)
		last_ts = int(messages[-1].timestamp)
		print('Batch [{0}/{1}]: {2} messages in this batch, {3} messages total'.format(i, n_batches, len(messages), len(all_messages)))
		time.sleep(1)
		if messages is None:
			output_obj(all_messages, fname=output_fname, invert_order=True)
			raise Exception('request failed ' + str(offset))
		all_messages.extend(messages)
		i += 1
except Exception as e:
	output_obj(all_messages, fname=output_fname, invert_order=True)
	raise(e)
output_obj(all_messages, fname=output_fname, invert_order=True)
print('Cleaning data')
sorted_messages = sorted(all_messages, key=lambda x: int(x.timestamp))
cleaned = []
i = 0
while i < len(sorted_messages):
	try:
		if sorted_messages[i-1].body != sorted_messages[i].body:
			cleaned.append(sorted_messages[i])
	except:
		cleaned.append(sorted_messages[i])
	i += 1
print('Number of clean messages:', len(cleaned))
print('Number of total messages:', len(all_messages))
output_obj(cleaned, output_fname.split('.')[0] + '_cleaned.pk')
