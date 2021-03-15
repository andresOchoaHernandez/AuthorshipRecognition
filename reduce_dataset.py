import glob
import os
import shutil

home_dir = os.environ["HOME"]

authors = [authors.replace(home_dir+ "/Dataset/","") for authors in glob.glob(home_dir + "/Dataset/*")]
books_per_author = {}


for author in authors:
	books_per_author[author] = len([elem for elem in glob.glob(home_dir + "/Dataset/"+ author+ "/*")])

books_per_author_sorted = sorted(books_per_author.items(), key=lambda x:x[1])

categories = {}

categories["1-10"] = 0
categories["10-20"] = 0
categories["20-30"] = 0
categories["30-40"] = 0
categories["40-50"] = 0
categories["50-60"] = 0
categories["60-70"] = 0
categories["70-80"] = 0
categories["80-90"] = 0
categories["90-100"] = 0

for elem in books_per_author_sorted:

	if elem[1] in range(1,11):
		categories["1-10"] += 1
	elif elem[1] in range(11,21):
		categories["10-20"] += 1
	elif elem[1] in range(21,31):
		categories["20-30"] +=1
	elif elem[1] in range(31,41):
		categories["30-40"] +=1
	elif elem[1] in range(41,51):
		categories["40-50"] +=1
	elif elem[1] in range(51,61):
		categories["50-60"] +=1
	elif elem[1] in range(61,71):
		categories["60-70"] +=1
	elif elem[1] in range(71,81):
		categories["70-80"] +=1
	elif elem[1] in range(81,91):
		categories["80-90"] +=1
	elif elem[1] in range(91,100):
		categories["90-100"] +=1

import matplotlib
import matplotlib.pyplot as plt

plt.bar(categories.keys(),categories.values())
plt.show()

# Media di libri per autore 3036 libri / 142 autori =  21.38 libri per autore
# Minimo numero di libri per autore 1, max 97