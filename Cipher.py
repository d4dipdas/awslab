def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")#ad EH#WX
    return stringToEncrypt
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")#4
    return shiftAmount
def encryptMessage(message, cipherKey, alphabet):#AD 4 A=ZA-Z#EH -4 A=ZA-Z
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()#AD#EH
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)#0#3#4
        newPosition = position + int(cipherKey)#0+4=4#3+4=7#0
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]#""+E+H#AD
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
def decryptMessage(message, cipherKey, alphabet):#EH,4 ,A=ZA-Z
    decryptKey = -1 * int(cipherKey)#-4
    return encryptMessage(message, decryptKey, alphabet)
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()
