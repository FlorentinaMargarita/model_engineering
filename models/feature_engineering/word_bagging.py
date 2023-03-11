from sklearn.feature_extraction.text import CountVectorizer


vectorizer = CountVectorizer()

def bag_of_words_func(messages):
    
    bagger = vectorizer.fit_transform(messages)
    vocabulary = list(vectorizer.vocabulary_.keys())
    print(vocabulary)
    # print("Bag of words matrix:\n", bagger.toarray())
    print(bagger, 'bagger')

    return bagger

# Print the vocabulary and the bag of words matrix
