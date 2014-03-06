#
# @ Federico Fancellu, 2014
#

# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib,urllib2
from pymongo import MongoClient
from nltk import pos_tag


class Wikictionary:

    def __init__(self):

        self.url = "http://en.wiktionary.org/w/api.php"
        client = MongoClient('localhost', 27017)
        self.db = client.apertium_database

        
        # {'english_word':
        #     {'korean':
        #         {'translation': 'a',
        #          'transl': 'b'},
        #     {'japanese':
        #         {'translation': 'a',
        #          'other': 'b'}
        #          }
        #         }
        #         

    def lookup_word(self,word):

        """Function to look up word in wikipedia to get inter-language links"""

        print repr(word)

        forms = {
            'format': 'xml',
            'action': 'query',
            'titles': word,
            'prop':'revisions',
            'rvprop':'content'
        }

        request = urllib2.Request(self.url,urllib.urlencode(forms))

        link = urllib2.urlopen(request)

        response = link.read()

        soup = BeautifulSoup(response)

        revision = soup.rev.string

        print revision

        return revision

    def isolate_trans(self,revision,*args):

        trans_index = revision.index('====Translations====')
        revision = revision[trans_index:]
        dnw = revision.index('\n\n')
        revision = revision[:dnw]

        trans_lines = dict()

        for lang in args:

            lang_dict = trans_lines.setdefault(lang,{})        

            trans = re.findall('\* ' + lang + r': (.+)',revision)[0]

            #TODO: just takes into consideration the 1st lexical translation
            trans = trans.split('}}, {{')[0]

            translation = trans.split('|')[2]
            lang_dict['translation'] = translation
                
            for _slice in trans.split('|')[3:]:

                print _slice

                if 'alt=' in _slice:
                    lang_dict['alt'] = _slice[_slice.index('=')+1:]
                    
                if 'tr=' in _slice:
                    lang_dict['tr'] = _slice[_slice.index('=')+1:]
                    

        return trans_lines

    def mongoDump(self,word,dictionary):

        complete_dict = {"word" : word, "translations": dictionary}
        bi_dict = self.db.bi_dict
        _id = bi_dict.insert(complete_dict)
        print _id



if __name__=="__main__":

    wk = Wikictionary()
    word = 'go'
    revision = wk.lookup_word(word)
    trans_lines = wk.isolate_trans(revision,'Korean','Japanese')
    pos = wk.pos_tagging(word)
    print pos
    #wk.mongoDump(word,trans_lines)

    #wk.extract_trans(trans_lines)
