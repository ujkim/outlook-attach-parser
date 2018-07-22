import openpyxl
import datetime
from listController import *

# about excel file management, it was implemented
class excelController(listController):
	def __init__(self):
		self.classtitle = "excelController"

	# customized (at fixed excel file format)
	def get_list_filtered_null_from_excel(self, attachmentFileList):
		for attachmentFileName in attachmentFileList:
			if '문지동' in attachmentFileName:
				attachmentFullPath = "/tmp/" + attachmentFileName
				wb = openpyxl.load_workbook(attachmentFullPath)
				ws = wb["주간메뉴표"]
				excelContentListExceptNull = list()
				for column in ws.columns:
					for cell in column:
						if cell.value is not None:
							excelContentListExceptNull.append(cell.value)
				return excelContentListExceptNull
	
	# below logic was implemented fixed with this cell format
	def get_dict_filtered_menu_along_date(self, excelContentsList):
		datetimeValidate_active = False
		menuContent_dict = dict()
		filteredMenuList = list()
		tmpDateTime_forTemp = ""
		for excelContent in excelContentsList:
			if isinstance(excelContent, datetime.datetime) or "점장" in excelContent:
				datetimeValidate_active = False
				if tmpDateTime_forTemp != "":
					menuContent_dict[tmpDateTime_forTemp] = list(filteredMenuList)
					filteredMenuList.clear()
			if datetimeValidate_active == True:
				filteredMenuList.append(excelContent)
				continue
			if isinstance(excelContent, datetime.datetime):
				tmpDateTime_forTemp = excelContent
				datetimeValidate_active = True
				continue
		return menuContent_dict


	# Along Time, Print Menu Munji Eat Menu
	# 0:Morning, 1:Lunch, 2:Night
	def print_today_menu_along_date(self, excel_date, menuContent_dict):
		exist_date_menu = False
		date = datetime.datetime.now() - datetime.timedelta(2)
		today_date = datetime.datetime.strptime(date.strftime('%Y-%m-%d'), '%Y-%m-%d')
		for key in menuContent_dict.keys():
			if key == today_date: #Today!
				if excel_date == 0: #Morning
					print("%s년 %s월 %s일 아침식단" % (today_date.year, today_date.month, today_date.day))
					for value in list(menuContent_dict[key])[0:5]:
						print(value)
					exist_date_menu = True
				if excel_date == 1: #Lunch
					print("%s년 %s월 %s일 점심식단" % (today_date.year, today_date.month, today_date.day))
					for value in list(menuContent_dict[key])[5:12]:
						print(value)
					exist_date_menu = True
				if excel_date == 2: #Night
					print("%s년 %s월 %s일 저녁식단" % (today_date.year, today_date.month, today_date.day))
					for value in list(menuContent_dict[key])[12:18]:
						print(value)
					exist_date_menu = True
		
		if exist_date_menu == False:
			print("오늘은 식사 일정이 없습니다.")

	# remove the excel attachment files
	def remove_excel_attachment_file(self, attachmentFileList):
		for attachmentFileName in attachmentFileList:
			attachmentFullPath = "/tmp/" + attachmentFileName
			if os.path.isfile(attachmentFullPath):
				os.remove(attachmentFullPath)
