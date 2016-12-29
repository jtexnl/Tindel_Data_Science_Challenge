import string
from spacy.en import English
from langdetect import detect

parser = English()

class review():
    
    def __init__(self, review_doc):
        self.text = self.process_text(review_doc['text'])
        self.parsed = self.parse(self.text)
        self.lemmatized = self.lemmatize(self.parsed)
        self.stars = review_doc['stars']

    def process_text(self, string_input):
        table = str.maketrans({key: None for key in string.punctuation})
        return string_input.translate(table).lower()

    def parse(self, text):
        try:
            return parser(text)
        except:
            return None

    def lemmatize(self, parsed):
        try:
            output = []
            for token in parsed:
                output.append(token.lemma_)
            return ' '.join(i for i in output)
        except:
            return None
        
class reviewSet():

    def __init__(self, business_list, canada = False):
        self.client = MongoClient()
        self.db = self.client.newYorkerTest
        self.reviews = self.db.reviews
        self.raw = self.pull_reviews(business_list, canada)
        self.features, self.labels = self.separate(self.raw)
        self.dict = {'features':self.features, 'labels':self.labels}

    def pull_reviews(self, business_list, canada):
        outList = []
        query = {'business_id':{'$in':business_list},'stars':{'$ne':3}}
        for i in self.reviews.find(query):
            if len(outList) <= 10000:
            #Note: here, I'm adding a piece of code for language detection, as I suspsect a good number of reviews from 
            #Quebec will be in French. Since SpaCy only has support for English (and since my assignment is for building an English-language ad campaign), 
            #we're going to skip over non-English reviews for now. If I were asked to run this exercise for a French- (or German)-language ad campaign, 
            #the slower NLTK package does have support for languages other than English, so we could use it instead. 
                try:
                    if canada:
                        if detect(i['text']) == 'en': 
                            outList.append(review(i))
                    else:
                        outList.append(review(i))
                except:
                    continue
        return outList

    def separate(self, raw):
        features = []
        labels = []
        for i in raw: 
            features.append(i.lemmatized)
            if i.stars >=4:
                labels.append(1)
            else:
                labels.append(0)
        return features, labels