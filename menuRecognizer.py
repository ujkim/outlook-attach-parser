import os, re
import config
from datetime import datetime

# this class works (about the already downloaded files, parsing and compare today
# this class was implementated with munji dir
# for added other dir, add the function
class menuRecognizer:
	def __init__(self):
		self.classtitle = "menuRecognizer"
		self.validExcelFileName = ""
	
	def getExcelFileName(self):
		return self.validExcelFileName

	def getConvertedDate(self, dateInfoList):
		# Make Str Date Info
		fromDateStr = str(datetime.today().year) + "." + dateInfoList[0]
		toDateStr = str(datetime.today().year) + "." + dateInfoList[-1]
		# Convert Str to Date
		fromDate = datetime.strptime(fromDateStr, '%Y.%m.%d')
		toDate = datetime.strptime(toDateStr, '%Y.%m.%d')
		return fromDate, toDate

	def IsExistIncludedExcel(self, FromDate, ToDate):
		TodayDate = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
		if TodayDate >= FromDate and TodayDate <= ToDate:
			return True
		else:
			return False

	# compare today info and
	def getValidExcelFileName(self, MenuFileNameList):
		date_regex = re.compile('\d+\.\d+\~\d+\.\d+')
		for MenuFileName in MenuFileNameList:
			dateInfoList = date_regex.findall(MenuFileName)[0].split('~')
			FromDateforExcel, ToDateforExcel = self.getConvertedDate(dateInfoList)
			if self.IsExistIncludedExcel(FromDateforExcel, ToDateforExcel) == True:
				return MenuFileName
		return None

	# validExcelFileName is None or FileName!
	def setValidExcelMenuFileName(self):
		MenuFileNameList = os.listdir(config.MUNJIURL)
		self.validExcelFileName = self.getValidExcelFileName(MenuFileNameList)
