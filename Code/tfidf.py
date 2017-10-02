# ARTIFICIAL INTELLIGENCE PROJECT - Automatic Story Summarization 

# ALGORITHM NAME - Automatic summarization based on weighting

#OWN
import nltk
from nltk.tokenize import RegexpTokenizer, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import operator
import matplotlib.pyplot as plt

stopwords = stopwords.words('english')

tokenizer = RegexpTokenizer(r'\w+')

stemmer = SnowballStemmer('english')

f1 = open('gift-of-magi.txt')
f2 = open('the-skylight-room.txt')
f3 = open('the-cactus.txt')

# OWN - read the files
text1 = f1.read()
text2 = f2.read()
text3 = f3.read()

# OWN - tokenize and form nltk objects
tk1 = nltk.Text(tokenizer.tokenize(text1))
tk2 = nltk.Text(tokenizer.tokenize(text2))
tk3 = nltk.Text(tokenizer.tokenize(text3))

# OWN - remove punctuations and digits and change to lower case
tk1 = [w.lower() for w in tk1 if w.isalpha() and not w.isdigit()]
tk2 = [w.lower() for w in tk2 if w.isalpha() and not w.isdigit()]
tk3 = [w.lower() for w in tk3 if w.isalpha() and not w.isdigit()]

# OWN - remove stop words and stem the words
tk1 = [stemmer.stem(w) for w in tk1 if w not in stopwords]
tk2 = [stemmer.stem(w) for w in tk2 if w not in stopwords]
tk3 = [stemmer.stem(w) for w in tk3 if w not in stopwords]

# OWN - find word frequencies
index1 = nltk.FreqDist(tk1)
index2 = nltk.FreqDist(tk2)
index3 = nltk.FreqDist(tk3)

# OWN - document frequencies
comb = index1.keys()
comb.extend(index2.keys())
comb.extend(index3.keys())
cindex = nltk.FreqDist(comb)

# OWN - split document into sentences
sent1 = sent_tokenize(text1)
sent2 = sent_tokenize(text2)
sent3 = sent_tokenize(text3)

# OWN - create word list of title
t1 = 'gift of magi'
t2 = 'the skylight room'
t3 = 'the cactus'
title1 = [stemmer.stem(w.lower()) for w in tokenizer.tokenize(t1) if w.isalpha() and w not in stopwords]
title2 = [stemmer.stem(w.lower()) for w in tokenizer.tokenize(t2) if w.isalpha() and w not in stopwords]
title3 = [stemmer.stem(w.lower()) for w in tokenizer.tokenize(t3) if w.isalpha() and w not in stopwords]

# OWN - calculate score for every sentence
scores1 = {}
sentence_lengths = []
for sentence in sent1:
	sentence_lengths.append(len(sentence))
	if len(sentence) < 81:
		# OWN - find all words in the sentence
		words = tokenizer.tokenize(sentence)
		words = [stemmer.stem(w.lower()) for w in words if w.isalpha() and not w.isdigit()]

		# OWN - sum of term frequencies and doc frequencies
		score = 0.0
		titlewords = 0.0
		for word in words:
			score = score + index1[word] / (1+cindex[word])
			if word in title1:
				titlewords += 1

		# OWN - number of words in sentence / number of those words present in title
		titlewords = 0.1 * titlewords / len(title1)
		scores1[sentence] = score + titlewords

scores2 = {}
sentence_lengths2 = []
for sentence in sent2:
	sentence_lengths2.append(len(sentence))
	if len(sentence) < 120:
		# OWN - find all words in the sentence
		words = tokenizer.tokenize(sentence)
		words = [stemmer.stem(w.lower()) for w in words if w.isalpha() and not w.isdigit()]

		# OWN - sum of term frequencies and doc frequencies
		score = 0.0
		titlewords = 0.0
		for word in words:
			score = score + index2[word] / (1+cindex[word])
			if word in title2:
				titlewords += 1

		# OWN - number of words in sentence / number of those words present in title
		titlewords = 0.1 * titlewords / len(title2)
		scores2[sentence] = score + titlewords

scores3 = {}
sentence_lengths3 = []
for sentence in sent3:
	sentence_lengths3.append(len(sentence))
	if len(sentence) < 90:
		# OWN - find all words in the sentence
		words = tokenizer.tokenize(sentence)
		words = [stemmer.stem(w.lower()) for w in words if w.isalpha() and not w.isdigit()]

		# OWN - sum of term frequencies and doc frequencies
		score = 0.0
		titlewords = 0.0
		for word in words:
			score = score + index3[word] / (1+cindex[word])
			if word in title3:
				titlewords += 1

		# OWN - number of words in sentence / number of those words present in title
		titlewords = 0.1 * titlewords / len(title3)
		scores3[sentence] = score + titlewords
'''
print scores1
sorted1 = sorted(scores1.items(), key = operator.itemgetter(1))
print sorted1[-10:]

f, axarr = plt.subplots(2, 2)

axarr[0, 0].hist(scores1.values(), bins = 30)
axarr[0, 0].set_title("Sentence lengths histogram")
# axarr[0, 0].xlabel('Number of characters')
# axarr[0, 0].ylabel('Number of sentences')
# axarr[0, 0].show()

axarr[0, 1].hist(scores2.values(), bins = 30)
axarr[0, 1].set_title("Sentence lengths histogram")
# axarr[0, 1].xlabel('Number of characters')
# axarr[0, 1].ylabel('Number of sentences')
# axarr[0, 1].show()

axarr[1, 0].hist(scores3.values(), bins = 30)
axarr[1, 0].set_title("Sentence lengths histogram")
# axarr[1, 0].xlabel('Number of characters')
# axarr[1, 0].ylabel('Number of sentences')
plt.show()
'''

# OWN - print the summary generated for each story
print 'gift of magi'
for sentence in scores1.keys():
	if scores1[sentence] >= 9:
		print sentence

print '\n\nthe skylight room'
for sentence in scores2.keys():
	if scores2[sentence] >= 19:
		print sentence

print '\n\nthe cactus'
for sentence in scores3.keys():
	if scores3[sentence] >= 2:
		print sentence