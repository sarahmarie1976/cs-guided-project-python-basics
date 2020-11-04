"""
Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"
Notes:

The input string will only contain alpha characters.
[execution time limit] 4 seconds (py3)

[input] string txt

[output] string

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name


"""

def csOppositeReverse(txt):

    # if a string return reverse order
    txt = txt[::-1] 
    txt = txt.swapcase()
    return txt

    # if a string  opposite casingreturn oppostie casing 

    


print(csOppositeReverse("Hello World"))   
print(csOppositeReverse("ReVeRsE"))
print(csOppositeReverse("Radar"))