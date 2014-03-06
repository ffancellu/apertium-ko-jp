#
# @ Federico Fancellu, 2014
#

# -*- coding: utf-8 -*-

from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from pymongo import MongoClient

class Processing:

    def __init__(self):

        self.lemmz = WordNetLemmatizer()
        client = MongoClient('localhost', 27017)
        self.db = client.apertium_database

    def tokenize_sentence(self,sentence):

        return word_tokenize(sentence)

    def get_word_pos(self,sent_tokens_list):

        return pos_tag(sent_tokens_list)

    def lemmatize_sentence(self,sentence_tok):

        return map(lambda x: self.lemmz.lemmatize(x),sentence_tok)

    def mongoDump(self,word,pos,dictionary):

        complete_dict = {"word" : word, "translations": dictionary,"pos": pos}
        bi_dict = self.db.bi_dict
        _id = bi_dict.insert(complete_dict)
        print _id

if __name__=="__main__":

    pr = Processing()
    sentence = "I was not at the cinema and cats came from all the ways."
    sent_tokens_list = pr.tokenize_sentence(sentence)
    print sent_tokens_list
    # tokens_to_tag = pr.lemmatize_sentence(sent_tokens_list)
    # print tokens_to_tag
    tagged_tokens=pr.pos_tagger(sent_tokens_list)
    print tagged_tokens

