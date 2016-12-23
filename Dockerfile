FROM python:3

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

RUN python -m spacy.en.download all

RUN apt-get update && apt-get install -y mongodb

RUN mkdir -p /data/db

EXPOSE 27017

ENTRYPOINT ["/usr/bin/mongod"]

RUN mongo --port 27017

RUN mongoimport --db newYorkerTest --collection reviews --drop --file yelp_academic_dataset_review.json