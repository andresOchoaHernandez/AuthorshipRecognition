import glob
import os
import shutil

books = [files for files in glob.glob("/home/andres/Gutenberg/txt/*.txt")]
books = [elem.replace("/home/andres/Gutenberg/txt/", "") for elem in books]

authors = [elem[:elem.find("_")] for elem in books]
authors = list(set(authors))
authors.sort()

books_per_author = {}
for author in authors:
	books_per_author[author] = [files for files in glob.glob("/home/andres/Gutenberg/txt/"+ author+"*.txt")]

os.mkdir("/home/andres/Dataset/")
for elem in authors:
	os.mkdir("/home/andres/Dataset/"+elem)

for key in books_per_author.keys():
	for path in books_per_author[key]:
		shutil.copyfile(path,"/home/andres/Dataset/"+key+"/"+ path.replace("/home/andres/Gutenberg/txt/", ""))
		
