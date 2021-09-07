import re 
import pandas as pd
import numpy as np  #for data to have numeric arrays
import json
import glob
import nltk
nltk.download("stopwords")

#Gensim
import gensim 
import gensim.corpora as corpora #helps with working with textual data
from gensim.utils import simple_preprocess # this simplepreprocess method of gensim helps in data pre-processing
from gensim.models import CoherenceModel # Objects of this class allow for building and maintaining a model for topic coherence

#spacy required for lemmatization)
import spacy
from nltk.corpus import stopwords #downloaded stopwords need to be imported


# import urllib library
from urllib.request import urlopen #only if I wamt to fetch a json from url

#visualizing LDA models in python
import pyLDAvis
import pyLDAvis.gensim_models
import pyLDAvis.gensim_models as gensimvis


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Preparing the data

#Json function 
def load_data(file):
    with open (file, "r", encoding="utf-8") as f:
        data = json.load(f) 
    return (data)

def write_data(file, data):
    with open (file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# reading the file
data = load_data(r'topic_modeling_files\topic_modeling_textbook-main\data\Testimonial dataset.json')["texts"][0:10]

#print (data[0][0:200])



#NLTK Stop words
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

# lemmatization function - reduction of words to its root form (we using spacy methof for lemma but it could also be done using nltk)
def lemmatization(texts, allowed_postags=["NOUN", "ADJ", "VERB", "ADV"]): #texts becuase we wanna iterate over all of our texts to lemmatize
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    texts_out = []
    for text in texts: #iterating over the text objects (250 testimonies)  
        doc = nlp(text)
        new_text = []
        for token in doc: #iterating over each of the word in all 250 testimonies 
            if token.pos_ in allowed_postags: # if its a noun,adj,verb,adverb , then apppend the lemma version of the word in newtxt empty list 
                new_text.append(token.lemma_)
        final = " ".join(new_text) # this displays all the lemmatized token string from into un-stringed form 
        texts_out.append(final) # this finally is printed inside a list
    return (texts_out)

lemmatized_texts = lemmatization(data)
#print (lemmatized_texts[5][0:220])    



# simplepreprocess converts the documents into tokens(tokenizes) into individual strings
def gen_words(texts):
    final = [] # we make this empty list to append in last step
    for text in texts: #iterating over all the texts 
        new = gensim.utils.simple_preprocess(text, deacc=True) # deacc is a boolean which reduces accent of other language in the text
        final.append(new)
    return (final)

data_words = gen_words(lemmatized_texts) # so we have normalized our lemmatized dataset 

print(data_words[5][0:220])

# a dictionary for looking up words and their frequency
id2word = corpora.Dictionary(data_words) # it will allow us to have few key pieces of data
corpus = []
for text in data_words:
    new = id2word.doc2bow(text) # create a bag of words. Also,it will contain a list of unique words with their frequency
    corpus.append(new)

#print (corpus[0][0:20])

word = id2word[[0][:1][0]]
#print (word)


# Building the model

# lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
#                                            id2word=id2word,
#                                            num_topics=30,
#                                            random_state=100,
#                                            update_every=1,
#                                            chunksize=100,
#                                            passes=10,
#                                            alpha="auto")

#visualizing the data



# vis =pyLDAvis.gensim.prepare(lda_model, corpus, id2word, mds="mmds", R=30)
# print(vis)

#lda_viz = gensimvis.prepare(lda_model, corpus, id2word)

#print(lda_viz)
