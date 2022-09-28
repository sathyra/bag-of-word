# corpus is a collection of documents, here sentences
panda= ['This is the first sentence in our learn panda followed by one more sentence to demonstrate Bag of words',
         'This is the second sentence in our learn panda with a FEW UPPER CASE WORDS and Few Title Case Words']

vocabulary = []         # empty list for vocabulary
total_words = 0    # to count total words in corpus

for doc in panda: # iterating through documents in corpus
    token_temp = doc.split() # create tokens
    total_words = total_words + len(token_temp)
    for i in range(len(token_temp)):
        if token_temp[i] not in vocabulary: # to check if word is already in vocab
            vocabulary.append(token_temp[i])

vocabulary.sort()

print(vocabulary) # Print all the words in vocabulary
print('There are {} words in vocabulary.'.format(len(vocabulary))) 
print('A total of {} words is used in documents.'.format(total_words))