#!/usr/bin/env python
# Copyright (c) 2022 Julian Fechner

import os

def main():
	# Specify exam name
	exam = "220-1102-messer-exam"
	# Combines the exam name for the different practice exams
	files = [exam + "-a", exam + "-b", exam + "-c"]

	# Loop through the files and add the different questions
	for i in range(len(files)):
		with open(files[i], "w") as f:
			x = 0
			for x in range(90):
				x += 1
				if files[i] == files[0]:
					f.write("A" + str(x) + "\n\n\n")
				elif files[i] == files[1]:
					f.write("B" + str(x) + "\n\n\n")
				elif files[i] == files[2]:
					f.write("C" + str(x) + "\n\n\n")

if __name__ == '__main__':
	main()