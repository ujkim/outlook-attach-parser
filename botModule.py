from strParser import *
from excelController import *
from listController import *

strParser = strParser()
excelCtrl = excelController()
listCtrl = listController()

# menutime infomation
# 0 : Breakfast, 1 : Lunch, 2 : Night
def load_content_along_time(mail, menutime):
	for Ids in mail.readIdsToday():
		mailContents = mail.getEmail(Ids)
		mailSubject = strParser.get_decoded_mail_contents(mail.mailsubject())
		if '주간식단' in mailSubject:
			if mail.saveAttachments(strParser, mailContents) == True:
				excelContentList = excelCtrl.get_list_filtered_null_from_excel(mail.attachmentList())
				excelContentList = listCtrl.get_list_remove_specific_str(excelContentList, " 쎄트렉아이 대전점")
				excelContentList = listCtrl.get_list_remove_specific_str(excelContentList, "최종한")
				filtered_menu_dict = excelCtrl.get_dict_filtered_menu_along_date(excelContentList)
				excelCtrl.print_today_menu_along_date(menutime, filtered_menu_dict)
				excelCtrl.remove_excel_attachment_file(mail.attachmentList())
			else:
				print("Save Attachment File Failed")
