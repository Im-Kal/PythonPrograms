# loop 100 times (i)
#   if i div 3 & 5 : print "FizzBuzz"
#   if i div 3: print "Fizz"
#   if i div 5: print "Buzz"

for i in range(1, 101):
    if i % 3 == 0 & i % 5 == 0:
        print("FizzBuzz")
    
    elif i % 3 == 0:
        print("Fuzz")
    
    elif i % 5 == 0:
        print("Buzz")
    
    else: 
        print(i)