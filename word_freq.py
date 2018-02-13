from read_obj import load_file
import sys
TOP_K = 1000
print('Loading...')
m = load_file(sys.argv[1])
print('Loaded')
word_table = {}
ignore_words = {'yeah', 'im', 'and', 'the', 'if', 'a', '-', '?', '!', '.', ',', 'this', 'that', 'but', 'her', 'his', 'an', 'for', 'he', 'she', 'it', 'their', 'there', 'i', 'is', 'to', 'you', 'in', 'of', 'was', 'are', 'on', 'have', 'not', 'so', 'just', 'my', 'me', 'we', 'at', 'be', 'do', 'with', "it's", 'they', 'can', 'now', 'should', 'or'}
names = {'himakar', 'sharma', 'adi', 'sahil', 'sony', 'ankit', 'akshay', 'nik', 'pranay', 'aditya', 'arnav', 'chris', 'nikhil', 'rishabh', 'salil', 'vinay', 'vishal', 'vish', 'yash', 'swapnil', 'swap', 'nikhilesh'}
print(len(m))
for message in m:
	m_body = message.text
	if m_body is None:
		continue
	for w in m_body.split():
		w = w.strip().lower()
		if w in ignore_words or w in names:
			continue
		if w in word_table:
			word_table[w] += 1
		else:
			word_table[w] = 1
word_list = sorted([(k,v) for k,v in word_table.items()], key=lambda x: x[1])[::-1][:TOP_K]

output_str = ''
for w,n in word_list:
	output_str += (w + ' ') * n
print(len(output_str))
with open('frequency_out.txt', 'w') as out_f:
	out_f.write(output_str)
