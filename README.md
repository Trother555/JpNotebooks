# JpNotebooks
My Jupyter notebooks for ML learning

In this notebook we compare 2 simple text classifiers. One is SVC and another is a neural network with few layers. We use NLTK and wordnet database for tokenization and lemmatization and sklearn's TfidfVectorizer and gensim's word2vec to vectorize words for models.
First we're going to load some labeled texts. Labels are 0 or 1 for negative or positive sentiment they express respectively. Then we'll brake texts into separate words, lemmatize and exclude stop-words. Next we'll train our models. SVC will use tfid vectorization, while neural natwork will deal with word2vec text representation model.
