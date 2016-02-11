# -*- coding: utf-8 -*-
import speech_recognition as sr

class VoiceRecognizer(object):

    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

    def speechToText(self):

        text = ""

        try:
            with self.m as source: self.r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(self.r.energy_threshold))

            print("Say something!")
            with self.m as source: audio = self.r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = self.r.recognize_google(audio)

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:    # this version of Python uses bytes for strings (Python 2)
                    text = format(value).encode("utf-8")
                    print(u"You said {}".format(value).encode("utf-8"))
                else:       # this version of Python uses unicode for strings (Python 3+)
                    text = format(value)
                    print("You said {}".format(value))

                return text

            except sr.UnknownValueError:
                return "Sorry, I can't undestand you!"
                
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                return "Sorry, I can't receive the google recognition response!"
        except KeyboardInterrupt:
            pass
