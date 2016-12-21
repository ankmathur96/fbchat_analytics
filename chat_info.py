import fbchat
import consts
import time
import pickle

LIMIT = 80
CHAT_ID = '100000054197818'
def output_obj(obj):
	obj = obj[::-1]
	with open('messages_' + CHAT_ID + '_early_june.pk', 'w') as out_f:
		pickle.dump(obj, out_f)

c = fbchat.Client(consts.username, consts.password)
all_messages = []
last_ts = 1465891200
for offset in range(110125, 160000, LIMIT):
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
output_obj(all_messages)
