# -*- coding:utf-8 -*-
import outlook
import config
import botModule

mail = outlook.Outlook()
mail.login(config.address, config.password)
mail.inbox()
mail.read()

botModule.load_content_along_time(mail, 1) #Lunch Menu!
botModule.load_content_along_time(mail, 2) #Night Menu!
botModule.load_content_along_time(mail, 0) #Breakfast Menu!

