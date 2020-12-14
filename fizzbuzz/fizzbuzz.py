#
# WRITTEN BY JAKE HENSON
# Written in Python
#
# fizzbuzz - a program that runs the classic game "fizbuzz"
# which will print "fizz" on multiples of three and "buzz" on multiples of five
# as well as "fizzbuzz" on multiples of both
# to run, type
# python fizzbuzz.py



#fizzbuzz takes in number of iterationsn and will print
#multiples of 3 with fizz and multiples of 5 with buzz, or both
# TIME COMPLEXITY - O(n)

def fizzbuzz(niters):
  for i in range(niters):
    #instantiating an output variable makes for better code
    #because it is more dynamic and can be tweaked easier
    output = ""
    if(i%3 == 0): output += "fizz"
    if(i%5 == 0): output += "buzz"
    elif (output == ""): output = i
    #checking to determine whether output is empty presents a simple solution because it makes the code
    #more dynamic

    print(output)


def main():
    fizzbuzz(100)

#probably depricated in python 3, but still worth looking into
if __name__ == "__main__":
    main()
