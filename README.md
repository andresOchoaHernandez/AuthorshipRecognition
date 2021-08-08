# AuthorshipRecognition
Final project for Big Data course in UNIVR.  
The goal of this project is to use the Gutenberg Dataset(https://web.eecs.umich.edu/~lahiri/gutenberg_dataset.html), split it into training and test, and extract writeprints of authors using SPARK. Finally use them to classify the test set.

# Instructions to execute the jupyter notebook
First of all, download the repo content and make sure to have SPARK and JUPYTER NOTEBOOK installed in your machine. Then you need to set the following variables:
```bash
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
```
Then launch spark:
```bash
SPARK_LOCAL_IP=127.0.0.1 ./bin/pyspark
```
Once the browser page opened, navigate to the folder of the repo and start the AuthorshipRecognitionPipeline notebook.
