# [Text Summarizer](https://en.wikipedia.org/wiki/Automatic_summarization)

## Description
Text Summary tool - a project which was part of Artificial Intelligence course at BITS Pilani 

## Algorithms

### 1.	[Automatic extraction based on weighting](http://research.nii.ac.jp/ntcir/workshop/OnlineProceedings3/NTCIR3-TSC-SekiY.pdf)
This approach treats sentences as ordered sequences and words as ordered sequences within sentences. It follows four fundamental steps:

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


### 2.	[Automatic Summary Extraction based on user query](http://ieeexplore.ieee.org/document/5270475/?reload=true)
This approach performs weighting of sentences based on the incoming user query. The weight of sentence is calculated using a mixture of 2 parameters. 

First, the weight of sentence obtained by tf-idf weighting. 

Second, the weight of query calculated using number of sentences the query occurs in. 

The combination of these 2 retrieves important phrases in the story relevant to the user query. This finds applications in creating a story search engine where a user can query for a story subject like “student wizard magic potions” and the search engine would present books like Harry Potter with a summary of the books extracted using this query. This will present the user with relevant stories and the part of the stories they are interested in.


### 3.	Information Extraction 
This method works in 2 phases. Selection of useful information and generation of a summary using the information. This improves upon the naïve automatic extraction technique by adding summary composition to create a more readable and coherent summary. 

The steps in this algorithm are:
-	Preprocess document to remove punctuations, bracket symbols, expand short form of some words.
-	Annotate each word with its part of speech information example if it is a noun/verb/adjective and so on.
-	Extract subject-verb-object triplets from each sentence.
-	Filter out triplets where verb is a past participle, infinitive, part of a conditional clause. These leads to false rejections as well which need to be controlled by correctly identifying triplets in multi verb sentences.
-	Generate noun phrases to represent subject, object, and indirect object of the sentences.
-	Generate a verb complement if no subject is present. Prepositional phrase generation for complementing noun phrases.
-	Generate verb phrase to link all components together.
-	Rank generated sentences using Document frequency of their terms.
-	Merge the sentence to form a summary. This is done by combining the generated sentences, then greedily pulling out subjects to see if the sentence can be reduced. This step uses a natural language generation engine.

This method captures the meaning of sentences by grammatical analysis which is why it is better than the automatic extraction approach. It can help in development of intelligent agents that gain better semantic knowledge of text.
