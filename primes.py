primes = []

def prime():
    for i in range(userinput1, userinput2 + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)

    print(primes)
    
userinput1 = int(input("Enter the 1st number = "))
userinput2 = int(input("Enter the 2nd number = "))

prime()
