'''
Function Name: Main
Function description: the purpose of this function is to call functions from local to open exist file. The
function will also start counting number of characters, words, and line when the file is successfully loaded.
Then it will start counting extra info like number of uppercase letter etc... In the end, it will out print
all the info with print function.
@param: none
@return: none    
'''

import print_me_first

def main():
    print_me_first.printinfo()
    uppercount = 0
    lowercount = 0
    spacecount = 0
    digitcount = 0
    sentencecount = 0
    mylist = [] #creating an empty list
    linecount,wordcount,charcount = counter('test.txt', mylist) #call function
    for line in mylist: #going thourgh all strings in list
        for char in line:
            if char.isupper(): #if the character that is reading from the line(string) is an uppercase letter
                uppercount = uppercount + 1 
            elif char.islower(): #if the character that is reading from the line(string) is lower case letter
                lowercount = lowercount + 1
            elif char.isspace(): #and so on...
                spacecount = spacecount + 1 
            elif char.isdigit():
                digitcount = digitcount + 1
            elif char == '.' or char == '!' or char == '?': #if one of them exist, it means there is a sentence
                sentencecount = sentencecount + 1;
                
    print('Total number of lines :', linecount)#outputing info
    print('Total number of words :', wordcount)
    print('Total number of characters :', charcount)
    print('Total number of uppercase letters :', uppercount)
    print('Total number of lowercase letters :', lowercount)
    print('Total number of spaces :', spacecount)
    print('Total number of digits :', digitcount)
    print('Total number of sentences :', sentencecount)

'''
Function Name: counter
Function description: the purpose of this function is to calculate numbers of characters, words, and line
and return them. The function will first open the file, error message will be displayed if failed. Then, it
will go line by line and start counting using while loop. While looping, it will also put every single line
of word into the list called lineList. In the end, info will be returned.

@param: filename - name of the file that is going to be opened
@param: lineList - a list that is holding all the line of words
@return: linecount - num of line
         wordcount - num of word
         charcount - num of character
'''
    
def counter(filename, lineList):
    
    linecount = 0 #initializing variables
    charcount = 0
    wordcount = 0
   
    line = ' '
    word = ' '
    
    try: #using try to prevent the IOError
        infile = open(filename,'r')
    except IOError:
        print('Error: can not file ', filename)
    else:
        line = infile.readline() #reading the first line from the file
        
    while line != '': #while there is still next line in the file
        linecount = linecount +1
        line = line.strip("\n") #taking off some white space
        print('Line ',linecount, ': ',line)
        charcount = charcount + len(line) #counting number of char in this line
        word = line.split() #turning a line to a list
        wordcount = wordcount + len(word) #counting number of word in that line   
        lineList.append(line) #adding the whole current line to the end of the list
        line = infile.readline() #moving to the next line
        
    infile.close()
    return linecount,wordcount,charcount

if __name__ == "__main__":
    main()
