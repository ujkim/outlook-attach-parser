#-*- coding: utf-8 -*-
import base64
import re, os
import quopri
from listController import *

# Parsing Function Related to String(Encrypted Email Contents) is implemented
class strParser(listController):
	def __init__(self):
		self.classtitle = "strParser"
	
	# mail string format : \" =?<charset>?<encoding>?<encoded-text>?= \"
	def get_decoded_words(self, encoded_words):
		encoded_word_regex = r'=\?{1}(.+)\?{1}([Bb|Qq])\?{1}(.+)\?{1}='
		charset, encoding, encoded_text = re.match(encoded_word_regex, encoded_words).groups()
		if encoding is 'B' or encoding is 'b':
			byte_string = base64.b64decode(encoded_text)
		elif encoding is 'Q' or encoding is 'q':
			byte_string = quopri.decodestring(encoded_text)
		if 'utf-8' in charset:	#added to utf-8 decoding error exception
			return byte_string.decode(encoding=charset, errors='ignore')
		return byte_string.decode(charset)

	# remove key in words	
	def get_words_remove_key(self, encoded_words, key):
		encoded_words = encoded_words.replace(key, "")
		return encoded_words

	# remove keywords in encoded_words
	# split along the line change key, get finally list(included with remove null)
	def get_list_filtered_field(self, encoded_words):
		encoded_words = self.get_words_remove_key(encoded_words, "\t")
		encoded_words = self.get_words_remove_key(encoded_words, "\r")
		encoded_words_list = encoded_words.split('\n')
		return self.get_list_removed_null(encoded_words_list)
	
	def get_merge_divided_lines(self, encoded_words_list, encoding_type):
		decoded_str = ""
		for str in encoded_words_list:
			if encoding_type == "Encrypt":
				decoded_str += self.get_decoded_words(str)
			elif encoding_type == "Normal":
				decoded_str += str
		return decoded_str

	# get decoded str along the encoding type,
	# return False : encoding type is not defined
	def get_decoded_str_along_encoding_type(self, encoded_words_list, encoding_type):
		if encoding_type == "Normal":
			return self.get_merge_divided_lines(encoded_words_list, encoding_type)
		elif encoding_type == "Encrypt":
			encoded_words_list = self.get_list_removed_empty_str(encoded_words_list)
			return self.get_merge_divided_lines(encoded_words_list, encoding_type)
		else:
			print("encoding type is not defined %s" % encoding_type)
		return False

	# In Mail List, there are some multiple type's mail
	# First of all, mail encoding format (get_decoded_words function, Distinguish =? string)
	# Second, norminal text
	# below function is filtering in this issue
	#  CASE1: as the string \n, divided string
	#  CASE2: only one line is included with full string
	# as a result, this function is return as value (divided encoded words is converted full decoded words)
	def get_decoded_mail_contents(self, encoded_words):
		finally_decoded_str = ""
		if '=?' in encoded_words: # encrypted encoding words
			if '\n' in encoded_words:
				encoded_words_list = self.get_list_filtered_field(encoded_words)
				finally_decoded_str = self.get_decoded_str_along_encoding_type(encoded_words_list, "Encrypt")
			else: # only one line
				finally_decoded_str = self.get_decoded_words(encoded_words)
		else:	# norminal text
			if '\n' in encoded_words:
				encoded_words_list = self.get_list_filtered_field(encoded_words)
				finally_decoded_str = self.get_decoded_str_along_encoding_type(encoded_words_list, "Normal")
			else: # only one line
				finally_decoded_str = encoded_words
		return finally_decoded_str
			
