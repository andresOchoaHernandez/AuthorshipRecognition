import glob
import os
import shutil

home_dir = os.environ["HOME"]

books = [files for files in glob.glob(home_dir + "/Gutenberg/txt/*.txt")]
books = [elem.replace(home_dir +"/Gutenberg/txt/", "") for elem in books]

authors = [elem[:elem.find("_")] for elem in books]
authors = list(set(authors))
authors.sort()

books_per_author = {}
for author in authors:
	books_per_author[author] = [files for files in glob.glob(home_dir +"/Gutenberg/txt/"+ author+"*.txt")]

os.mkdir(home_dir +"/Dataset/")
for elem in authors:
	os.mkdir(home_dir +"/Dataset/"+elem)

for key in books_per_author.keys():
	for path in books_per_author[key]:
		shutil.copyfile(path,home_dir +"/Dataset/"+key+"/"+ path.replace(home_dir +"/Gutenberg/txt/", ""))
		
