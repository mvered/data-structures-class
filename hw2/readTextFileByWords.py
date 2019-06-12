"""
    File:  readTextFileByWords.py
    Description:  Simple program to demonstrate how to:
    * read a text file a line at a time
    * split each line by white-space (space, tab) into a list of words
    * print each word
"""
from os.path import exists

def main():
    fileName = input("Enter file name to split into words (e.g., aTextFile.txt): ")

    if not exists(fileName):
        print("File", fileName, "does NOT exist!")
    else:
        # Open the file for reading 'r'
        myFile = open(fileName, 'r')
        lineNumber = 1
        # loop over the file a line at a time
        for line in myFile:
            line = line.strip() # remove new-line character from line
            print('Words on line %d: "%s"' % (lineNumber, line)) 
            # split line by default of white-space
            wordList = line.split()

            # loop over list of words and print each word
            for word in wordList:
                print(word)
            lineNumber += 1

            
main()
