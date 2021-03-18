import glob
import os
import shutil
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def print_dict ( mydictionary ):
	for key in mydictionary.keys():
		print(key + " : " + str(mydictionary[key]))


def create_books_per_author(home_dir,authors):
	books_per_author = {}

	for author in authors:
		books_per_author[author] = len([elem for elem in glob.glob(home_dir + "/Dataset/"+ author+ "/*")])

	return books_per_author

def extract_categories(books_per_author_sorted):
	categories = {}
	for elem in books_per_author_sorted :
		if str(elem[1]) not in categories.keys():
			categories[str(elem[1])]=1
		else:
			categories[str(elem[1])]+=1 

	return categories

def plot_bar(x,y,labelx,labely,yticks):
	plt.bar(x,y)
	plt.xlabel(labelx)
	plt.ylabel(labely)
	plt.yticks(yticks)
	plt.show()

def plot_lin(x,y,labelx,labely,xticks,yticks):
	plt.plot(x,y)
	plt.xlabel(labelx)
	plt.ylabel(labely)
	plt.xticks(xticks) 
	plt.yticks(yticks)
	plt.grid()
	plt.show()

if __name__ == "__main__":

	home_dir = os.environ["HOME"]

	authors = [authors.replace(home_dir+ "/Dataset/","") for authors in glob.glob(home_dir + "/Dataset/*")]


	books_per_author = create_books_per_author(home_dir,authors)
	books_per_author_sorted = sorted(books_per_author.items(), key=lambda x:x[1])
	categories = extract_categories(books_per_author_sorted)


	plot_bar(categories.keys(),categories.values(),"Number of books","Number of authors",np.arange(1,13,1))

	treshold ={}
	disc_authors = 0

	treshold[0]=142

	treshold_books_loss = {}
	treshold_books_loss[0] = 3036
	disc_books = 0

	for th in range(1,16):

		disc_authors += categories[str(th)]
		treshold[th] = 142 - disc_authors
		disc_books+= th * categories[str(th)]
		treshold_books_loss[th] = 3036 - disc_books

	x = [elem for elem in treshold.keys()]
	y = [elem for elem in treshold.values()]

	plot_lin(x,y,"Treshold","Authors",np.arange(0,16,1),np.arange(61,143,3))

	x = [elem for elem in treshold_books_loss.keys()]
	y = [elem for elem in treshold_books_loss.values()]

	plot_lin(x,y,"Treshold","Books",np.arange(0,16,1),np.arange(2520,3037,12))

