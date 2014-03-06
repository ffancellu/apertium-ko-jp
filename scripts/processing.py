#
# @ Federico Fancellu, 2014
#

# -*- coding: utf-8 -*-

from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer

class Processing:

	def __init__(self):

		self.lemmz = WordNetLemmatizer()

	def tokenize_sentence(self,sentence):

		return word_tokenize(sentence)

	def pos_tagger(self,sent_tokens_list):

		return pos_tag(sentence)

	def lemmatize_sentence(self,sentence_tok):

		return map(lambda x: self.lemmz.lemmatize(x),sentence_tok)

if __name__=="__main__":

	pr = Processing()
	sentence = "I was not at the cinema and cats came from all the ways."
	sent_tokens_list = pr.tokenize_sentence(sentence)
	print sent_tokens_list
	tagged_tokens = pr.lemmatize_sentence(sent_tokens_list)
	print tagged_tokens
