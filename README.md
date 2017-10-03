# text-summarizer
Text Summary tool - a project which was part of Artificial Intelligence course at BITS Pilani 

Algorithms used:

1.	Automatic extraction based on weighting [1]: This approach treats sentences as ordered sequences and words as ordered sequences within sentences. It follows four fundamental steps:

o	Weighting of words
o	Weighting of sentences
o	Choosing all sentences above a certain weight threshold
o	Ordering the selected sentences as they appear in the original article

The approach of weighting is based on frequencies. Every word/term is assigned a weight using tf-idf (term frequency – inverted document frequency) approach. The weight of a term = term frequency * inverse of document frequency

Term frequency is the number of a times a word occurs within a document. 
Inverted document frequency is 1 / number of documents the words appears in.

Additionally the score incorporates parameters like location of the word, syntactic structure of the sentence in which it appears, presence of the word in title etc.
Each sentence is assigned a weight equal to the sum of weights of the words.
Once all sentences are weighted, they are sorted in descending order of their weights. A certain threshold is set on the weight of a sentence that can be in a summary and then the sentences are filtered.
The filtered sentences are put in the original order as they appear in the document. This approach is a statistical method that purely relies on term level content of the story. This method involves preprocessing on terms like removing stop words, normalizing terms, replacing synonyms etc.

