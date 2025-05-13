from stats import word_count, character_count, sorted_dic
import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	# path = 'books/frankenstein.txt'
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path = sys.argv[1]
	book_text = get_book_text(path)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")

	count = word_count(book_text)
	print("----------- Word Count ----------")
	print(f"Found {count} total words")

	count_chars = character_count(book_text)
	sorted_char_list = sorted_dic(count_chars)
	print("--------- Character Count -------")
	for item in sorted_char_list:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")


main()