## How to run the code

### Docker

In order to run the code in this repo, you will need to first have [Docker](https://docs.docker.com/engine/installation/) installed and set up on your computer. 

### Data

While most of this package is self-contained in Docker, you will need to have the dataset, which can't be stored in this repo. You should download the Yelp dataset from [this link](https://www.yelp.com/dataset_challenge/dataset) and store it in the directory with the rest of the code from this repo. You will only need the 'yelp_academic_dataset_review.json' file. If you need to move it from your downloads folder (from this repo folder), the command is:

```mv path/to/downloads/yelp_academic_dataset_review.json . ```

Once you build the docker image, a Mongodb instance will be created, and the dataset will be inserted into the database for use in the code.

### Starting the Program

Once you have cloned the repo, downloaded the data, and moved it to the folder where the code is, type ```docker-build compose``` to begin the setup process. This will take some time. 

Once the docker file has built, type ```docker-compose build``` and another set of dowloads will start. Once they are complete, type ```docker-compose up``` and follow the link that is displayed in stdout to your localhost instance where the notebook should be visible. 