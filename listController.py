
from strParser import *

# about list contents management was implemented
class listController:
	def __init__(self):
		self.classtitle = "listController"

	# remove empty string at string list (\" \" remove)
	def get_list_removed_empty_str(self, encoded_words_list):
		removed_emptylist = list()
		for str in encoded_words_list:
			replaced_str = str.replace(" ", "")
			removed_emptylist.append(replaced_str)
		return removed_emptylist

	# remove null string at string list (null, None remove)
	def get_list_removed_null(self, encoded_words_list):
		encoded_words_list = filter(None, encoded_words_list)
		return encoded_words_list

	# remove specific string
	def get_list_remove_specific_str(self, Input_list, specific_str):
		Input_list.remove(specific_str)
		return Input_list
