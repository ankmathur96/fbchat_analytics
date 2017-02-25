from read_obj import load_file

m = load_file(sys.argv[1])
word_table = {}
ignore_words = {'and', 'the', 'if', 'a', '-', '?', '!', '.', ',', 'this', 'that', 'but', 'her', 'his', 'an', 'for', 'he', 'she', 'it', 'their', 'there'}
for message in m:
	for w in message:
		w = w.strip().lower()
		if w in ignore_words:
			continue
		if w in word_table:
			word_table[w] += 1
		else:
			word_table[w] = 1
