# -*- coding:utf-8 -*-
import outlook
import config
import botModule
from menuRecognizer import *

menuRec = menuRecognizer()
mail = outlook.Outlook()
mail.login(config.address, config.password)
mail.inbox()
mail.read()

menuRec.setValidExcelMenuFileName()
ValidExcelFileName = menuRec.getExcelFileName()
if ValidExcelFileName == None: # No Menu
	print("No Menu")
else:# if exists with menu, parse & print
	botModule.load_content_along_time(ValidExcelFileName, 0)

#botModule.load_content_along_time(ValidExcelFileName, 1) #Lunch Menu!
#botModule.load_content_along_time(ValidExcelFileName, 2) #Night Menu!
#botModule.load_content_along_time(ValidExcelFileName, 0) #Breakfast Menu!

