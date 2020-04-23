# Assignment 5 - Part-of-Speech Tagging using HMMs and Viterbi Algorithm

In this assignment, you'll be implementing a POS Tagger based on HMMs and implement Viterbi algorithm. 

## Working Files: 

You will be restricted to work only with 'viterbi.py' file. Reading and writing of data has been done for you. You need to implement the following two functions in the file - 

- store_emission_and_transition_probabilities
- assign_POS_tags

Follow the instructions given in comments. 

## Data:

The training corpus contains words that can be classified as any one of the following 12 universal tags - 

VERB - verbs (all tenses and modes)  
NOUN - nouns (common and proper)  
PRON - pronouns  
ADJ - adjectives  
ADV - adverbs  
ADP - adpositions (prepositions and postpositions)  
CONJ - conjunctions  
DET - determiners  
NUM - cardinal numbers  
PRT - particles or other function words  
X - other: foreign words, typos, abbreviations  
. - punctuation  

## Deliverables: 

You need to implement aforementioned two functions in 'viterbi.py'. Up on successful execution, results on the public test dataset will be displayed on your screen and a file 'output.txt' will be generated. Make sure that your code is running and 'output.txt' is generated before submission. 

## Hint File: 

Refer to 'hint.pdf' to understand the intuition and mathematics behind Viterbi algorithm. 

All the best. 
