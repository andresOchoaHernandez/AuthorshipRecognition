import glob
import os
import shutil
import sys
import math   

def print_dict ( mydictionary ):
	for key in mydictionary.keys():
		print(key + " : " + str(mydictionary[key]))

if __name__ == "__main__":

	if (len(sys.argv) == 1 or len(sys.argv)>=3) or (int(sys.argv[1])<1 or int(sys.argv[1])>100):
		print("Expected at least and at most one integer argument between 1 and 100 !")
		print("Usage: split_dataset <percentage of training set>") 
		exit(-1)

	training = int(sys.argv[1])
	test = 100 - training

	#Creating a dictionary that holds the number of books for each author according to the training-test percentage
	home_dir = os.environ["HOME"]

	authors = [authors.replace(home_dir+ "/Dataset/","") for authors in glob.glob(home_dir + "/Dataset/*")]
	books_per_author = {}
	for author in authors:
		books_per_author[author] = len([elem for elem in glob.glob(home_dir + "/Dataset/"+ author+ "/*")])

	
	books_per_author_training_set = {}

	for author in books_per_author.keys():
		books_per_author_training_set[author] = math.ceil(books_per_author[author] * training / 100)


	# Creating a function that selects the first number of books calculate before of each author

	#colelction with all books for every author
	books_for_each_author = {}
	for author in authors:
		books_for_each_author[author] = [elem for elem in glob.glob(home_dir + "/Dataset/"+ author+ "/*")]


	training_set = {}
	test_set = {}

	for author in books_for_each_author.keys():		
		training_set[author] = [books_for_each_author[author][index] for index in range(1,books_per_author_training_set[author]+1)]
		test_set[author] = [books_for_each_author[author][index] for index in range(books_per_author_training_set[author]+1,len(books_for_each_author[author]))]

	#writing out the folders
	os.mkdir(home_dir +"/training_set/")
	for elem in training_set.keys():
		os.mkdir(home_dir +"/training_set/"+elem)
	
	for key in training_set.keys():
		for path in training_set[key]:
			shutil.copyfile(path,home_dir + "/training_set/"+key+"/"+path.replace(home_dir+"/Dataset/",""))
	
	os.mkdir(home_dir +"/test_set/")
	for elem in test_set.keys():
		os.mkdir(home_dir +"/test_set/"+elem)
		
	for key in test_set.keys():
	for path in test_set[key]:
		shutil.copyfile(path,home_dir + "/test_set/"+key+"/"+path.replace(home_dir+"/Dataset/",""))
	# Creating a function that selects randomly the number of books calculate before of each author
	# TODO
