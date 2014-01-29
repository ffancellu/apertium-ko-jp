#-*- coding: utf-8 -*-

class Break:

	def __init__(self):

		self.lead_start = int(0x1100) - 1
		self.vowel_start = int(0x1161) - 7 
		self.tail_start = int(0x11a8) - 1

		self.START = 44032

	def break_const(self,word):

		array_ch = list()

		for block in word.decode('utf8'):

			print repr(block)

			if block != u' ':

				tail = self.get_tail(block)
				print tail
				vowel = self.get_vowel(block,ord(tail))
				print vowel
				lead = self.get_lead(block)
				print lead

				array_ch.extend([lead,vowel,tail])

			elif block == u' ': array_ch.append(u' ')

		return array_ch

	# def ud(self,inp):

	# 	return inp.decode('cp949')

	def get_tail(self,block):

		return unichr(self.tail_start + ((ord(block) - self.START) % 28))

	def get_vowel(self,block,tail):

		#vowel = 1 + mod (Hangul codepoint − 44032 − tail, 588) / 28
		return unichr(self.vowel_start + (1 + (((ord(block) - 44032 - tail) % 588) / 28)))

	def get_lead(self,block):

		#lead = 1 + int [ (Hangul codepoint − 44032)/588 ]
		return unichr(self.lead_start + (1 + int((ord(block) - 44032) / 588)))

class Conversion:

	def __init__(self):

		self.table = {
			#initial ㅇ
			u'\u110b' : '',
			#empty tail
			u'\u11a7' : '',
			#white space
			u' ' : ' ',
			#consonants
			u'\u1100' : 'g',#lead ㄱ
			u'\u11a8' : 'k',#tail ㄱ
			u'\u1101' : 'kk',#lead ㄲ
			u'\u11a9' : 'k',#tail ㄲ
			u'\u11aa' : 'ks',
			u'\u1102' : 'n',#lead ㄴ
			u'\u11ab' : 'n',#tail ㄴ
			u'\u1103' : 'd',#lead ㄷ
			u'\u11ae' : 't',#tail ㄷ
			u'\u1104' : 'tt',#ㄸ
			u'\u1105' : 'r',#lead ㄹ
			u'\u11af' : 'r',#tail ㄹ
			u'\u11b0' : 'lk',
			u'\u11b1' : 'lm',
			u'\u11b2' : 'lp',
			u'\u11b3' : 'ls',
			u'\u11b4' : 'lt',
			u'\u11b5' : 'lp',
			u'\u11b6' : 'lh',
			u'\u1106' : 'm',#lead ㅁ
			u'\u11b7' : 'm',#tail ㅁ
			u'\u1107' : 'b',#lead ㅂ
			u'\u11b8' : 'p',#tail ㅂ
			u'\u1108' : 'pp',#ㅃ
			u'\u11b9' : 'ps',
			u'\u1109' : 's',#lead ㅅ
			u'\u11ba' : 's',#tail ㅅ
			u'\u110a' : 'ss',#lead ㅆ
			u'\u11bb' : 'ss',#tail ㅆ
			u'\u11bc' : 'ng',#tail ㅇ
			u'\u110c' : 'j',#lead ㅈ
			u'\u11bd' : 't',#tail ㅈ
			u'\u110d' : 'jj',#ㅉ
			u'\u110e' : 'ch',#lead ㅊ
			u'\u11be' : 't',#tail ㅊ
			u'\u110f' : 'k',#lead ㅋ
			u'\u11bf' : 'k',#tail ㅋ
			u'\u1110' : 't',#lead ㅌ
			u'\u11C0' : 't',#tail ㅌ
			u'\u1111' : 'p',#lead ㅍ
			u'\u11c1' : 'p',#tail ㅍ
			u'\u1112' : 'h',#lead ㅎ
			u'\u11c2' : 'h',#tail ㅎ
			#vowels
			u'\u1161' : 'a',
			u'\u1162' : 'ae',
			u'\u1163' : 'ya',
			u'\u1164' : 'yae',
			u'\u1165' : 'eo',
			u'\u1166' : 'e',
			u'\u1167' : 'yeo',
			u'\u1168' : 'ye',
			u'\u1169' : 'o',
			u'\u116a' : 'wa',
			u'\u116b' : 'wae',
			u'\u116c' : 'oe',
			u'\u116d' : 'yo',
			u'\u116e' : 'u',
			u'\u116f' : 'weo',
			u'\u1170' : 'we',
			u'\u1171' : 'wi',
			u'\u1172' : 'yu',
			u'\u1173' : 'eu',
			u'\u1174' : 'yi',
			u'\u1175' : 'i',
			#bugs
			u'\u1160' : 'i',
			u'\u115e' : 'eu',
			u'\u115f' : 'yi'
			#TO DO:mapping this other range to the vowels

		}

	def table_lookup(self,array_ch):

		return map(lambda x: self.table[x],array_ch)
