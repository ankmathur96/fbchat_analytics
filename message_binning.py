import sys
import pickle
import datetime
import json
fname = sys.argv[1]
SECONDS_IN_DAY = 86400
with open(fname, 'r') as in_file:
	messages = pickle.load(in_file)
chart_data = []
first_ts = messages[0].timestamp
first_ts_date = datetime.date.fromtimestamp(int(first_ts) / 1000)
# crop time to find midnight
first_ts_date = datetime.datetime(first_ts_date.year, first_ts_date.month, first_ts_date.day, 8, 0, 0)
# convert to epoch
cur_ts_epoch = (first_ts_date - datetime.datetime(1970,1,1)).total_seconds()
next_ts_epoch = cur_ts_epoch + SECONDS_IN_DAY
current_count = 0
prev_index = 0
for i, m in enumerate(messages):
	# timestamp in seconds
	m_ts = int(m.timestamp) / 1000
	if m_ts > cur_ts_epoch and m_ts < next_ts_epoch:
		current_count += 1
	elif m_ts >= next_ts_epoch:
		if current_count > 1000:
			print('********************************' + '---' + str(current_count))
			for j in range(prev_index, i):
				try:
					print(messages[j].body.encode("utf-8") + ' ' + str(messages[j].timestamp))
				except Exception:
					print('FAILED MESSAGE PRINT')
					pass
			print('********************************')
		chart_data.append({'timestamp' : cur_ts_epoch, 'count' : current_count})
		cur_ts_epoch = next_ts_epoch
		next_ts_epoch = cur_ts_epoch + SECONDS_IN_DAY
		prev_index = i
		current_count = 1
with open(fname.split('.')[0] + '_json.json', 'w') as out_f:
	json.dump(chart_data, out_f)