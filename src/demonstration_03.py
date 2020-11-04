"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

how would we cast string to integer 

We would instantiate an int object from the string data example --- int("10")
    then it will return an integer   -- 10
if we check the type(int("10")) 
<class 'int'>   

We can use  the int() constructor to convert other data types to an Interger



Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
# def string_int(txt):
#     # Your code here
#     #sent number to the int value to txt

#     number = int(txt)

#     # return number
#     return number


def string_int(txt):
   

    # return the int value of text to the caller
    return int(txt)

print(string_int("6"))
print(string_int("1000"))
print(string_int("12"))



