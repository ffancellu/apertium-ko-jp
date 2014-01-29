#-*- coding: utf-8 -*-

from conversion import *

def main():

	chop = Break()
	convert = Conversion()
	array_ch = chop.break_const('의자 그소효')
	print array_ch
	conv_chrs = ''.join(filter(lambda x: x!='',convert.table_lookup(array_ch)))
	print conv_chrs

if __name__=="__main__":

	main()



