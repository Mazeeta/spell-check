#!/usr/bin/env python

import language_check

def spellCheck(text):
	langTool = language_check.LanguageTool('en-US')
	matches = langTool.check(text)
	totalErrorWords = len(matches)
	print ('Total number of error words :: ' + str(totalErrorWords))
	print ('*' * 80, end='\n\n')
	
	# prints the description of errored words and its suggested words
	for match in matches:
		print (match)
		print ('*' * 80, end='\n\n')
	
	correctedText = language_check.correct(text, matches)
	return correctedText

if __name__ == '__main__':
	erroredText = input('Enter the text to check spelling :: ') # What is the most baeutiful thing in the worlld?
	correctedText = spellCheck(erroredText)
	print ('Corrected text :: ' + str(correctedText))
	
