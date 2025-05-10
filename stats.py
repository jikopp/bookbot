def word_count(text):
	words = text.split()
	return len(words)

def character_count(text):
	text = text.lower()
	chars_count = {}
	for char in text:
		if char in chars_count:
			chars_count[char] += 1
		else:
			chars_count[char] = 1
	return chars_count
	
def sorted_dic(dict):
	sorted_chars = []
	for char, count in dict.items():
		if char.isalpha():
			sorted_chars.append({"char": char, "num": count})
	sorted_chars.sort(key=lambda item: item["num"], reverse=True)
	return sorted_chars