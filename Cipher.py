# File: Cipher.py

# Description: Encrypts message by turning block of characters right and decrypts by turning block left


def findBlockSize(userWord):

    #this function determines the length and width that the block is going to be
    blockSize = len(userWord)
    while blockSize % (blockSize ** 0.5) != 0:  #While blockSize is not a perfect square
        blockSize += 1
    blockSize = int(blockSize ** 0.5)
    return blockSize


def fillBlockEn(userWord, blockSize):

        #this function fills in the block for encryption with the appriopriate word and block size
        wordList = []
        for letter in userWord:
            wordList.append(letter)
        yList = []
        n = 0

        #this loop adds values to the block, and adds a * for each space in which the block is longer than the word
        for y in range(blockSize):
            xList = []
            for x in range(blockSize):
                if n > len(wordList) - 1:
                    xList.append('*')
                else:
                    xList.append(wordList[n])
                n += 1
            yList.append(xList)
        return yList

def fillBlockDe(userWord, blockSize):

    # Fills in the block for prior to decryption
    myList = []
    numspaces = blockSize**2 - len(userWord)

    #Creates a 2d array of the correct dimensions containing - as each value
    for x in range(blockSize):
        tempList = []
        for y in range(blockSize):
            tempList.append('-')
        myList.append(tempList)

    #Changes the - to * in the correct location. The amount of astericks is how much larger the block is than the word
    for col in range(blockSize):
        for row in reversed(range(blockSize)):
            if numspaces > 0:
                myList[row][col] = '*'
                numspaces = numspaces - 1

    #Fills in the values of the user word into the decrypted location on the block.
    currentPosition = len(userWord)
    for i in reversed(range(blockSize)):
        for j in reversed(range(blockSize)):
            if myList[i][j] == '-':
                myList[i][j] = userWord[currentPosition - 1]
                currentPosition = currentPosition - 1
    return myList

def encryption(blockList, blockSize):

    #This function turns the block 90 degrees right.
    newListY= []

    #Creates a blank block of the correct dimensions
    for j in range(blockSize):
        newListX = []
        for i in range(blockSize):
            newListX.append("")
        newListY.append(newListX)

    #Adds values of old array into correct position in new array so it appears that the array was turned right
    for row in range(0, blockSize):
        for col in range(0, blockSize):
            newListY[col][blockSize-row-1] = blockList[row][col]
    newListY = ''.join(str(letter) for list in newListY for letter in list) #list to string
    encryptedWord = newListY.replace("*","") #removes * in output
    print(encryptedWord)

def decryption(blockList, blockSize):

    #The function turns the array 90 degrees left.
    newListY = []

    # Creates a blank block of the correct dimensions
    for j in range(blockSize):
        newListX = []
        for i in range(blockSize):
            newListX.append("")
        newListY.append(newListX)

    # Adds values of old array into correct position in new array so it appears that the array was turned left
    for row in range(0, blockSize):
        for col in range(0, blockSize):
            newListY[row][col] = blockList[col][blockSize - row - 1]
    newListY = ''.join(str(letter) for list in newListY for letter in list) #list to string
    decryptedWord = newListY.replace("*", "")  #removes * in output
    print(decryptedWord)

def main():

    userEncryption = []
    encryptedMessage = open("encrypt.txt", "r")
    fileLines = encryptedMessage.readlines()
    encryptedMessage.close()
    for line in fileLines:
        userEncryption.append(line.strip('\n'))
    numMsgEn = int(userEncryption[0])

    userDecryption = []
    decryptedMessage = open("decrypt.txt", "r")
    fileRead = decryptedMessage.readlines()
    decryptedMessage.close()
    for row in fileRead:
        userDecryption.append(row.strip('\n'))
    numMsgDe = int(userDecryption[0])

    if numMsgEn < 1 or numMsgEn > 100:
        print("Error. Please make sure the number of messages to encrypt is from 1-100.")
        exit()

    if numMsgDe < 1 or numMsgDe > 100:
        print("Error. Please make sure the number of messages to decrypt is from 1-100.")
        exit()

    userEncryption.pop(0)
    print("Encryption:")
    for message in userEncryption:
        if len(message) < 1 or len(message) > 100:
            print("Error. Message must be 1-100 characters.")
            exit()
        blockEn = findBlockSize(message)
        encryption(fillBlockEn(message, blockEn),blockEn)

    userDecryption.pop(0)
    print("\nDecryption:")
    for word in userDecryption:
        if len(word) < 1 or len(word) > 100:
            print("Error. Message must be 1-100 characters.")
            exit()
        blockDe = findBlockSize(word)
        decryption(fillBlockDe(word, blockDe),blockDe)


main()
