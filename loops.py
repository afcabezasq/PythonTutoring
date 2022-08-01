def loops():

    myCharacters = 'abcdefglmnopq'

    myList = list(myCharacters)

    myDictionary = { 'a':85 , 'b':65, 'c':78, 'd':106, 'g':58}

    print(myDictionary)

    for key in myDictionary:
        
        if key == 'b':
            continue
        print(key+"  "+str(myDictionary[key])) 

    number = 5
    counter = 0

    # while counter<len(myList):

    #     print(myList[counter])
    #     counter = 1 + counter





if __name__ == '__main__':
    loops()