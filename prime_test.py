

def is_prime(n):
    counter = 0

    if n == 1 or n == 0:
        return False
    
    for i in range(2,n+1):
        if n%i == 0:
            counter += 1
    
    if counter == 1:
        return True
    else:
        return False


def primes():
    number = int(input("Write a number: "))

    if is_prime(number):
        print("This is prime")
    else:
        print("Not prime number")

if __name__ == '__main__':
    primes()