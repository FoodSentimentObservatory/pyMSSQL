from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.datasets import load_files
import numpy as np

def display_topics(H, W, feature_names, no_top_words, no_top_documents):
    for topic_idx, topic in enumerate(H):
        print ('Topic %d:' % (topic_idx))
        print (' '.join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))
        print ("-- -- -- -- -- -- -- -- -- -- -- -- --")


path = input("Please provide a directory: ")
if len(path)==0:

    path = '/some/default/path'

dataset = load_files(path, description=None, categories=None, load_content=True, shuffle=True, encoding=None, decode_error='strict', random_state=0)
documents = dataset.data

no_features = 1000


# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names()

no_topics = 50


# Run LDA
lda_model = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)
lda_W = lda_model.transform(tf)
lda_H = lda_model.components_

no_top_words = 20
no_top_documents = 1
print ("-----------------------------------")
display_topics(lda_H, lda_W, tf_feature_names, no_top_words, no_top_documents)
l = dir(lda_model)

