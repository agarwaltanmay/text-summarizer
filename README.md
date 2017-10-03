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


2.	Automatic Summary Extraction based on user query [3]: This approach performs weighting of sentences based on the incoming user query. The weight of sentence is calculated using a mixture of 2 parameters. 

First, the weight of sentence obtained by tf-idf weighting. 

Second, the weight of query calculated using number of sentences the query occurs in. 

The combination of these 2 retrieves important phrases in the story relevant to the user query. This finds applications in creating a story search engine where a user can query for a story subject like “student wizard magic potions” and the search engine would present books like Harry Potter with a summary of the books extracted using this query. This will present the user with relevant stories and the part of the stories they are interested in.

