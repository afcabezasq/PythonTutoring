
import numbers


def read():
    numbers = []
    with open("./archives/numbers.txt",'r') as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers


def write():
    names = ["Alex","Felix","Aaron","John","Ferdinand"]
    with open("./archives/names.txt","a") as namesFile:
        for name in names:
            namesFile.write(f"{name} \n")

def priceTable():
    prices = read()
    products = ["wrench","cell phone","laptaop","pan","mouse","ladder","mixer","knife set","pots","towells"]
    with open("./archives/listProducts.csv","w") as productList:
        productList.write("Product, Price \n")
        for i in range(0,10):
            productList.write(f"{products[i]}, {prices[i]} \n")
    
    

def main():
    read()
    write()
    priceTable()

if __name__ == '__main__':
    main()
