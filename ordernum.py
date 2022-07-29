primes = [2, 3, 5, 7]

def check():
    min = primes[0]
    max = primes[0]

    for i in primes:
        if i > max:
            max = i

        if i <= min:
            min = i

    print("Minimum: ", min, "Maximum", max)