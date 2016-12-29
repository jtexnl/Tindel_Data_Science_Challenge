from classes import reviewSet
from pymongo import MongoClient
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics

def pull_classify_and_dump(dataset, name, canada = False):
    reviews = reviewSet(dataset, canada)
    if len(reviews.dict['labels']) < 100:
        print('Insufficient Data. Please try a different location.')
    else:
        vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
        classifier = SGDClassifier(alpha = .0001, n_iter = 10, penalty = 'L2')
        X = vectorizer.fit_transform(reviews.dict['features'])
        classifier.fit(X, reviews.dict['labels'])
        joblib.dump(vectorizer, name + '_vectorizer.pkl')
        joblib.dump(classifier, name + '_classifier.pkl')
        joblib.dump(dataset, name + '_dataset.pkl')
        del reviews

def reload(region):
    vectorizer = joblib.load(region + '_vectorizer.pkl')
    classifier = joblib.load(region + '_classifier.pkl')
    return vectorizer, classifier

def n_most_least_positive(region, n, print_output = True):
    vectorizer, classifier = reload(region)
    feature_names = vectorizer.get_feature_names()
    top_n = np.argsort(classifier.coef_[0])[-n:]
    bottom_n = np.argsort(classifier.coef_[0])[:n]
    positive_words = (feature_names[j] for j in top_n)
    negative_words = (feature_names[j] for j in bottom_n)
    if print_output:
        print('Top ' + str(n) + ' most positively-associated words in region: ' + region)
        print('------------------------------------------------------------------------')
        print(list(positive_words))
        print('            ')
        print('Top ' + str(n) + ' most negatively-associated words in region: ' + region)
        print('------------------------------------------------------------------------')
        print(list(negative_words))
    return positive_words, negative_words

def top_n_by_region(inputData, name, n, states = True, cities = False, check_english = False):
    client = MongoClient()
    db = client.newYorkerTest
    businesses = db.businesses
    print("Running business database query")
    cursor = businesses.find().limit(1000000)
    region_businesses = []
    print("Filtering database response")
    if states:
        for element in cursor:
            if states:
                if type(inputData) is list:
                    if element['state'] in inputData:
                        region_businesses.append(element['business_id'])
                elif type(inputData) is str:
                    if element['state'] == inputData:
                        region_businesses.append(element['business_id'])
    if cities:
        for element in cursor:
            if type(inputData) is list:
                if element['city'] in inputData:
                    region_businesses.append(element['business_id'])
            elif type(inputData) is str:
                if element['city'] == inputData:
                    region_businesses.append(element['business_id'])
    print("Running Review Database Query...This may take some time")
    pull_classify_and_dump(region_businesses, name, check_english)
    print("Running Classifier")
    n_most_least_positive(name, n, print_output = True)