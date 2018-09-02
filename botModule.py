from strParser import *
from excelController import *
from listController import *
import os
import datetime
import config

strParser = strParser()
excelCtrl = excelController()
listCtrl = listController()

# 0 : Breakfast, 1 : Lunch, 2 : Night
def load_content_along_time(ValidExcelFileName, menutime):
	excelContentList = excelCtrl.get_single_list_filtered_null_from_excel(ValidExcelFileName)
	excelContentList = listCtrl.get_list_remove_specific_str(excelContentList, " 쎄트렉아이 대전점")
	excelContentList = listCtrl.get_list_remove_specific_str(excelContentList, "최종한")
	filtered_menu_dict = excelCtrl.get_dict_filtered_menu_along_date(excelContentList)
	excelCtrl.print_today_menu_along_date(menutime, filtered_menu_dict)
