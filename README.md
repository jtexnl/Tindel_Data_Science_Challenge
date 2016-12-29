#Introduction

This repository represents my (John Tindel's) submission to New Yorker in support of my candidacy for the role of data scientist. The goal of the exercise was to, given a set of data from Yelp, come up with some interesting questions around the data and write a program using data science techniques to answer the question. 

The question I chose to answer was whether there were regional variations in how people express positive/negative sentiments. I will explore this question in-depth in the Jupyter notebook found in this repo, or you can run my CLI tool for getting the top n positive/negative words for a given geographic area by following the setup instructions below.

# How to run the code

This repo contains two major components: a Jupyter notebook that allows the user to explore my thought process in putting this exercise, as well as a CLI tool that serves as a proof of concept for how a tool like this might work. Nothing is required if you want to view the notebook: Github will show all of my work and its output. 

If you would like to employ my CLI tool (which is currently very much a proof-of-concept, not a production model), follow the steps below to prepare your environment. I have included instructions for users who would like to use Docker and those who would prefer not to.

## With Docker

In order to run the code in this repo, you will need to first have [Docker](https://docs.docker.com/engine/installation/) installed and set up on your computer. 

### Data

While most of this package is self-contained in Docker, you will need to have the dataset, which can't be stored in this repo (both due to its size and due to the Yelp ToS). You should download the Yelp dataset from [this link](https://www.yelp.com/dataset_challenge/dataset) and store it in the directory with the rest of the code from this repo. You will only need the 'yelp_academic_dataset_review.json' file. If you need to move it from your downloads folder (from this repo folder), the command is:

```mv path/to/downloads/yelp_academic_dataset_review.json . ```

Once you build the docker image, a Mongodb instance will be created, and the dataset will be inserted into the database for use in the code.

### Starting the Program

Once you have cloned the repo, downloaded the data, and moved it to the folder where the code is, type ```docker-build compose``` to begin the setup process. This will take some time, as the composition will involve migrating a very large file to MongoDB and the installation of some large libraries from SpaCy. 

Once the docker file has built, type ```docker-compose build``` and another set of dowloads will start. The CLI should eventually open the program and you will see the instruction prompts. If this fails, try following the non-Docker instructions to install/download.

## Without Docker

If you want to run this without docker, you will need to have Mongodb and Python 3.4+ (and pip) installed on your machine. Once Mongodb is set up and configured, open a tab in your terminal and type ```mongod``` to start your mongo engine. 

Next, download the dataset available at [this link](https://www.yelp.com/dataset_challenge/dataset). Once you've expanded the file, cd into that directory and type the following command to move the data to the proper collection in Mongo: 

```mongoimport --db newYorkerTest --collection reviews --drop --file yelp_academic_dataset_review.json```

Now, you'll need to install your basic requirements. From this repo's local folder, type ```pip install -r requirements.txt``` (remember, if Python 2.x is your default implementation, type ```pip3 install -r requirements.txt``` so that the files go to the right root directory) to dowload the required Python libraries. Once that's done, you'll also need to install the Spacy data for lemmatization. Type ```python -m spacy.en.download all``` (or ```python3 -m spacy.en.download all``` if 2.x is your default) to begin the Spacy data download. Once that's done, the final step is to run ```jupyter notebook```, and a web browser should take you to a localhost instance of this repo. Click on ```Tindel_New_Yorker_Data_Science_Challenge.ipynb``` to view/run the presentation. 