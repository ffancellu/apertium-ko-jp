#
# @ Federico Fancellu, 2014
#

# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib,urllib2


class Wikictionary:

    def __init__(self):

        self.url = "http://en.wiktionary.org/w/api.php"

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

        return revision

    def isolate_trans(self,revision,*args):

        trans_index = revision.index('====Translations====')
        revision = revision[trans_index:]
        dnw = revision.index('\n\n')
        revision = revision[:dnw]

        trans_lines = list()

        for lang in args:

            print lang
        
            trans_lines.append(re.findall(r'\* ' + lang + r': \{\{(.+)\}\}',revision)[0])

        return trans_lines
        
    def extract_trans(self,trans_lines):

        translations = map(lambda x: x.split('|')[2],trans_lines)
        translit = map(lambda x: x.split('|')[3],trans_lines)

        return translations, translit

if __name__=="__main__":

    wk = Wikictionary()
    revision = wk.lookup_word('rain')
    trans_lines = wk.isolate_trans(revision,'Korean','Japanese')
    wk.extract_trans(trans_lines)
