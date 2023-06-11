# fizzbuzz - a program that runs the classic game "fizbuzz"
# which will print "fizz" on multiples of three and "buzz" on multiples of five
# as well as "fizzbuzz" on multiples of both
# to run, type
# python fizzbuzz.py

#
# WRITTEN BY Jackie Henson
# Written in Python
#



#fizzbuzz takes in number of iterations and will print
#multiples of 3 with fizz and multiples of 5 with buzz, or both


def fizzbuzz(numIterations):
  for i in range(numIterations):
    output = ""     #instantiating an output variable makes for better code, because it is more dynamic and can be tweaked easier

    if(i%3 == 0): output += "fizz"
    if(i%5 == 0): output += "buzz"
    elif (output == ""): output = i
    #checking to determine whether output is empty presents a simple solution because it makes the code
    #more dynamic

    print(output)


def main():
    fizzbuzz(100)

#at this point, main is
# likely depricated in python 3, worth looking into for later versions - regardless, my algorithm here is what's on display
if __name__ == "__main__":
    main()


# TIME COMPLEXITY - O(n)