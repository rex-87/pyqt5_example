# -*- coding: utf-8 -*-
"""
	PyQt5 Example
	
	This project gives an overview of a PyQt5 working environment.
"""

## -------- COMMAND LINE ARGUMENTS ---------------------------
## https://docs.python.org/3.7/howto/argparse.html
import argparse
CmdLineArgParser = argparse.ArgumentParser()
CmdLineArgParser.add_argument(
	"-v",
	"--verbose",
	help = "display debug messages in console",
	action = "store_true",
)
CmdLineArgs = CmdLineArgParser.parse_args()

## -------- LOGGING INITIALISATION ---------------------------
import misc
misc.MyLoggersObj.SetConsoleVerbosity(ConsoleVerbosity = {True : "DEBUG", False : "INFO"}[CmdLineArgs.verbose])
LOG, handle_retval_and_log = misc.CreateLogger(__name__)

try:
	
	## -------------------------------------------------------
	## THE MAIN PROGRAM STARTS HERE
	## -------------------------------------------------------	

	import sys
	from PyQt5 import QtWidgets
	from PyQt5 import uic

	class MyDialog(QtWidgets.QDialog):
		
		def __init__(self):
			
			super(MyDialog, self).__init__()
			dialog = uic.loadUi("pyqt5_example\pyqt5_example.ui", self)
			dialog.show()
		
		def say_hello(self, user_text):
			
			text = "Hello there, {0}!".format(user_text)
			self.label_3.setText(text)

	app = QtWidgets.QApplication(sys.argv)
	dialog = MyDialog()
	app.exec_()

## -------- SOMETHING WENT WRONG -----------------------------	
except:

	import traceback
	LOG.error("Something went wrong! Exception details:\n{}".format(traceback.format_exc()))

## -------- GIVE THE USER A CHANCE TO READ MESSAGES-----------
finally:
	
	input("Press any key to exit ...")
