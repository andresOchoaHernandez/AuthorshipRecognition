import glob
import os
import shutil
import sys

def print_dict ( mydictionary ):
	for key in mydictionary.keys():
		print(key + " : " + str(mydictionary[key]))

if __name__ == "__main__":

	if len(sys.argv) == 1 or len(sys.argv)>=3:
		print("Expected at least and at most 1 argument!")
		print("Usage: reduce_dataset_by_treshold <value of treshold>") 
		exit(-1)

	TRESHOLD = int(sys.argv[1])

	home_dir = os.environ["HOME"]
	authors = [authors.replace(home_dir+ "/Dataset/","") for authors in glob.glob(home_dir + "/Dataset/*")]

	books_per_author = {}
	for author in authors:
		books_per_author[author] = len([elem for elem in glob.glob(home_dir + "/Dataset/"+ author+ "/*")])

	authors_cancelled = []

	for author in books_per_author.keys() :
		if books_per_author[author] < TRESHOLD:
			authors_cancelled.append(author)

	for author in authors_cancelled:
		print("Deleting folder of the author "+ author)
		shutil.rmtree(home_dir + "/Dataset/"+ author)


