
def fibo(number):
    if number == 0 or number == 1:
        return 1    
    return fibo(number-1) + fibo(number-2)



def fibonacci(number):
    n = number-1
    return fibo(n)


if __name__ == "__main__":
    print(fibonacci(6))