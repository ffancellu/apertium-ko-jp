#
# @ Federico Fancellu, 2014
#

# -*- coding: utf-8 -*-

import wikitionary
# import codecs

def main():

    wiki = wikitionary.Wikictionary()

    # english = codecs.open('../resources/brit-a-z.txt','rb',encoding='utf-8')
    english = open('../resources/brit-a-z.txt','rb')

    for word in english:

        word = word[:-2]

        print 'looking at word...',repr(word)

        try:

            revision = wiki.lookup_word(word)
            trans_lines = wiki.isolate_trans(revision,'Korean','Japanese')
            wiki.mongoDump(word,trans_lines)

        except:

            print 'Word does not exist'

    english.close()

if __name__=="__main__":

    main()





