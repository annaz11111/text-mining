import numpy as np
import os
import sys
import nltk
import gensim
import pickle
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

file_docs = []

#Import and tokenize sentences
with open('book_review.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file_docs.append(line)

# print("Number of documents:", len(file_docs)) 

#Create dictionaries of tokenized words
gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in file_docs]
# print(gen_docs)

#Convert words to unique ids to work with genism
dictionary = gensim.corpora.Dictionary(gen_docs)
# print(dictionary.token2id) 

#Create a bag of words 
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
# print(corpus)

#Term Frequency (TF-IDF): Words that occur more frequently across the documents get smaller weights
tf_idf = gensim.models.TfidfModel(corpus)
for doc in tf_idf[corpus]:
    print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])

#Creat similarity measure object 
sims = gensim.similarities.Similarity('assignment2',tf_idf[corpus], num_features=len(dictionary))

'''After index built, 
calculate how similar the book review is to the movie review'''

file2_docs = []

#Open and load the movie review file
with open ('movie_review.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file2_docs.append(line)

for line in file2_docs:
    query_doc = [w.lower() for w in word_tokenize(line)]
    query_doc_bow = dictionary.doc2bow(query_doc) #update an existing dictionary and create bag of words

# perform a similarity query against the corpus
query_doc_tf_idf = tf_idf[query_doc_bow]

#Average similarity of documents
sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))

#Average similarity of documents
percentage_of_similarity = round(float((sum_of_sims / len(file_docs)) * 100))



if __name__ == "__main__":
#Print tokenized file
    print("Number of documents:",len(file2_docs))
# print(document_number, document_similarity)
print('Comparing Result:', sims[query_doc_tf_idf])  
print(sum_of_sims)
#Printverage similarity of documents
print(f'Average similarity float: {float(sum_of_sims / len(file_docs))}')
print(f'Average similarity percentage: {float(sum_of_sims / len(file_docs)) * 100}')
print(f'Average similarity rounded percentage: {percentage_of_similarity}')
