# TODO1: convert allText to a single string which has all the strings appended
# (ex) ['I', 'am', 'healthy'] becomes "I am healthy"

# TODO2: fill in the body of the for loop here then answer to the google form question


from nltk import tokenize
import nltk


allText = [x.strip()
           for x in open("Course-Evaluation.csv", encoding='utf8').readlines()]

# convert allText to a single string to count word frequencies with nltk library
allText_to_string = ''  # TODO1: change the right-hand side properly


# tokenize allText and count the frequencies
wordList = tokenize.word_tokenize(allText_to_string)
len(wordList)

# count the word frequencies and store it to a dictionary d
d = nltk.FreqDist(wordList)


# print out the word frequencies
for key in d:
    # TODO2: fill in the body of the for loop here then answer to the google form question
    print('')
