FROM python:3

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

RUN python -m spacy.en.download all

RUN mongod

RUN mongoimport --db newYorkerTest --collection reviews --drop --file yelp_academic_dataset_review.json