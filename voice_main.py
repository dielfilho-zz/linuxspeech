# -*- coding: utf-8 -*-
from command_handler import CommandHandler
import thread
import time


com = CommandHandler()
while com.handle():
	time.sleep(0.5)
