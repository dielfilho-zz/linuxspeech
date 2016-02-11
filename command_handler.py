# -*- coding: utf-8 -*-

import subprocess
import shlex
from voice_recognizer import VoiceRecognizer
from espeak import espeak 
from action_manager import ActionManager

class CommandHandler(object):

	CONST_TURN_OFF = "turn off"
	CONST_TURN_ON = "turn on"
	CONST_GOODBYE = "goodbye"

	def __init__(self):

		espeak.synth("Hello Master!")

		self.rec = VoiceRecognizer()

		self.actions = ActionManager().loadActions()

		self.canHear = True;

	def callSubProcess(self, args, text):
		try:
			espeak.synth(text)
			args = args.split(" ")
			subprocess.Popen(args)
		except Exception as e:
			print "Error on callSubProcess: "+str(e)
			espeak.synth("Sorry, I can't "+text)

	def handle(self):
		voiceCommand = self.rec.speechToText().lower()
		if voiceCommand != "":
			if self.CONST_TURN_OFF in voiceCommand:
				espeak.synth("Turning off the microphone")
				self.canHear = False
			elif self.CONST_TURN_ON in voiceCommand:
				espeak.synth("Turning on the microphone")
				self.canHear = True
				return True

			if self.canHear:
				if self.CONST_GOODBYE in voiceCommand:
					espeak.synth("bye")
					return False

				espeak.synth("You said "+voiceCommand)
				for action in self.actions:
					if voiceCommand in action.voiceCommand:
						self.callSubProcess(action.args, "Executing "+voiceCommand)		
				

		return True
