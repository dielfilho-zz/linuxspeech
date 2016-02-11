# -*- coding: utf-8 -*-
from command_handler import CommandHandler
import thread
import time


com = CommandHandler()
# Sleep a half of second for others computations
while com.handle():
	time.sleep(0.5)
