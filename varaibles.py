
def main1():
    print("My function")

    number = 12
    number2 = 12.3
    character = "My character"
    character1 = "My character +"+str(number)

    character2 = f" My character2 hold number: {number}"

    character3 = f"""
        My numbers are the folowing:    {number}
                                        {number2}
    """

    character4 = f'''
    My numbers are the folowing:    {number}
                                        {number2}
    '''

    myEmptyList = []
    my_list = [1,5,'myFirstString','dogs', myEmptyList]

    dictionary = { 'a':1,'b':2}
    t = (4,5)
    dictionary[t] = "myValue"
    # print(number)
    # print(number2)
    # print(character)
    # print(character1)
    # print(character2)
    print(character3)


if __name__ == '__main__':
    main1()