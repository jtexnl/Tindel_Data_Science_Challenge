# Tindel_Data_Science_Challenge

## How to run the code

### Docker

In order to run the code in this repo, you will need to first have [Docker](https://docs.docker.com/engine/installation/) installed and set up on your computer. 

### Data

While most of this package is self-contained in Docker, you will need to have the dataset, which can't be stored in this repo. You should download the Yelp dataset from [this link](https://www.yelp.com/dataset_challenge/dataset) and store it in the directory with the rest of the code from this repo. You will only need the 'yelp_academic_dataset_review.json' file. If you need to move it from your downloads folder (from this repo folder), the command is:

```mv path/to/downloads/yelp_academic_dataset_review.json . ```

Once you build the docker image, a Mongodb instance will be created, and the dataset will be inserted into the database for use in the code.

### 
