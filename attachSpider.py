# -*- coding:utf-8 -*-
import outlook
import config
from strParser import *
from excelController import *
from listController import *
import os, re
from datetime import datetime

strParser = strParser()
excelCtrl = excelController()
listCtrl = listController()

# Comparision with downloaded file and attach name
def IsFileInAttachWithStr(partStr, attachFileName,  downCompletedList):
	for downFileName in downCompletedList:
		if partStr in attachFileName and attachFileName == downFileName:
			print("%s file exists in there" % attachFileName)
			return True
	return False

# get the Munji, Junmin file exists flag
def IsExistsAttachment(attachmentList):
	IsMunjiExistAttachmentFlag = False
	IsJunminExistAttachmentFlag = False
	downedMunjiFileNames = os.listdir(config.MUNJIURL)
	downedJunminFileNames = os.listdir(config.JUNMINURL)
	for attachFileName in attachmentList:
		IsMunjiExistAttachmentFlag = IsFileInAttachWithStr("문지동", attachFileName, downedMunjiFileNames)
	for attachFileName in attachmentList:
		IsJunminExistAttachmentFlag = IsFileInAttachWithStr("전민동", attachFileName, downedJunminFileNames)
	return IsMunjiExistAttachmentFlag, IsJunminExistAttachmentFlag
	
# save with along the flag(munji, junmin)
def saveAttachAlongFlag(mail, mailSubject, mailContents, Flag):
	if Flag == False:
		mail.saveAlongMunjiJunmin(strParser, mailContents)
	else:
		print("%s file already exists on directory" % mailSubject)

def downloadMailAttachment():
	mail = outlook.Outlook()
	mail.login(config.address, config.password)
	mail.inbox()
	mail.read()
	attachmentList = list()
	for Ids in mail.readIdsToday():
		mailContents = mail.getEmail(Ids)
		mailSubject = strParser.get_decoded_mail_contents(mail.mailsubject())
		if '주간식단' in mailSubject:
			# get attachmentList, first! check in menu directory if it's exists or not.
			# if it's not exists in, download attachment file!
			# if it's exists in, don't do that.
			attachmentList.clear()
			attachmentList = mail.getAttachmentList(strParser, mailContents)
			MunjiFlag, JunminFlag = IsExistsAttachment(attachmentList)
			saveAttachAlongFlag(mail, mailSubject, mailContents, MunjiFlag)
			saveAttachAlongFlag(mail, mailSubject, mailContents, JunminFlag)

downloadMailAttachment()
