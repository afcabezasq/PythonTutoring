from rooms import Room as R


def house():
    myRoom1 = R("Michael", 20, 30)
    myRoom2 = R("Sam",10,15)
    myRoom3 = R("Michaela",12,17)

    print(myRoom1,myRoom2,myRoom3)



if __name__ == '__main__':
    house()