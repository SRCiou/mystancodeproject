"""
File: boggle.py
Name: Ruby
----------------------------------------
TODO:
"""

import time
all_word = []
# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	ans = []
	input_lst = []
	read_dictionary()
	for i in range(4):
		row = input('low of letters: ')
		if len(row) != 7:
			print('illegal format')
			break
		else:
			for j in range(len(row)):
				if i % 2 != 0:
					if row[i] != ' ':
						print('illegal format')
						return
		input_lst.append(row.split())

	find_word(input_lst, ans)
	print('There are', len(ans), 'words in total.')
	start = time.time()
	####################
	read_dictionary()

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(input_lst, ans):

	for i in range(4):
		for j in range(4):
			order = [(i, j)]
			find_word_helper(i, j, order, input_lst, input_lst[i][j], ans,)


def find_word_helper(x, y, order, input_lst, start, ans_lst,):
	if len(start) >= 4:
		if start in all_word:
			if start not in ans_lst:
				ans_lst.append(start)
				print(start)
	# Recursion
	for j in range(-1, 2):
		for k in range(-1, 2):
			start_x = x + j
			start_y = y + k
			# choose
			if start_x >= 0 and start_x < 4 and start_y >= 0 and start_y < 4:
				if (start_x, start_y) not in order:
					start += input_lst[start_x][start_y]
					order.append((start_x, start_y))
					# print(ans)
					if has_prefix(start):
						# Explore
						find_word_helper(start_x, start_y, order, input_lst, start, ans_lst,)
					# Un-choose
					start = start[:-1]
					order.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global all_word
	with open(FILE, 'r') as f:
		for line in f:
			all_word.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in all_word:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
