#
# @ Federico Fancellu, 2014
#

# -*- coding: utf-8 -*-

import wikitionary
import processing
import codecs

def main():

    wiki = wikitionary.Wikictionary()
    pr = processing.Processing()

    # english = codecs.open('../resources/brit-a-z.txt','rb',encoding='utf-8')
    english = codecs.open('../resources/europarl-v7.fr-en.en','rb',encoding='utf-8')

    for sent in english:

        sent_token_list = pr.tokenize_sentence(sent)
        word_pos = pr.get_word_pos(sent_token_list)

        for item in word_pos:

            if pr.db.bi_dict.find_one({'word':item[0]})==None:

                print 'looking at word...',repr(item[0])

                try:

                    revision = wiki.lookup_word(item[0])
                    trans_lines = wiki.isolate_trans(revision,'Korean','Japanese')
                    pr.mongoDump(item[0],item[1],trans_lines)

                except:

                    print 'Word does not exist'

    english.close()

if __name__=="__main__":

    main()





