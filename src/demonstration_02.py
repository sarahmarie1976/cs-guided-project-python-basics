"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

write a function that takes an integer showing minutes and converts minutes to seconds

Examples:
- convert(5) ➞ 300     (this is 5 * 60 = 300 -> because there is 60 seconds in a minute)
- convert(3) ➞ 180     (this is 3 * 60  -> because there is 60 seconds in a minute)
- convert(2) ➞ 120     (this is 2 * 60  -> because there is 60 seconds in a minute)

 # we can times minutes by 60 to get seconds 

 # You could define a function with an int

 # -> is a straight arrow and is a returning value annotation, with is part of function annotation and it's a feature of Python 3 

# example:

 # def convert(minutes:int) -> int:             you can have the output what you ever you like but the question 
  #                                           sounds like it is asking for an integer.

"""
# def convert(minutes:int):
#     # Your code here
#     # set seconds to the value of the expression minutes * 
    
#     seconds = minutes * 60

#     return seconds


# print(convert(5))
# print(convert(3))
# print(convert(2))



def convert(minutes:int):
    # Your code here
    
    return minutes * 60

print(convert(5))
print(convert(3))
print(convert(2))

