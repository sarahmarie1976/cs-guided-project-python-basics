"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

We can loop over string....

set an "o" and "x" counter to zero
Loop over each character in the string
do a check if it contains an "x"
    increment the "x" counter
do a check if it contains an "o"
    increment the "o" counter

check if "x" counter is equal to "o" counter 
    if it is then return true to the caller
otherwise we can return false to the caller


Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
# def XO(txt:str) -> bool:
#     # set an "o" and "x" counter to zero

#     o_counter = 0
#     x_counter = 0

#     # Loop over each character in the string

#     for char in txt: 
        
#         if char == "x":                 # do a check if it contains an "x"
#             x_counter += 1              # increment the "x" counter 

#         elif char == "X":                 # do a check if it contains an "X"
#             x_counter += 1              # increment the "x" counter           

#         elif char == "o":               # do a check if it contains an "o"
#              o_counter += 1             # increment the "o" counter

#         elif char == "o":               # do a check if it contains an "o"
#              o_counter += 1             # increment the "o" counter      

#     if x_counter == o_counter:          # check if "x" counter is equal to "o" counter 
#         return True                     # return true to the caller
#     else:                               # otherwise we can 
#         return False                    # return false to the caller 


# def XO(txt:str) -> bool:
#     # set an "o" and "x" counter to zero

#     o_counter = 0
#     x_counter = 0

#     # Loop over each character in the string

#     for char in txt: 
        
#         if char == "x" or char == "X":                 # do a check if it contains an "x" or "X"
#             x_counter += 1                             # increment the "x" counter 

#         elif char == "o" or char == "O":               # do a check if it contains an "o" or "O"
#              o_counter += 1                            # increment the "o" counter

     
#         # return x counter i s equal to o counter as a boolean to the caller

#     return x_counter == o_counter      

def XO(txt:str) -> bool:
        #  lowercase the txt
        
    lower_txt = txt.lower()

        # return the count of lower txt using "x" as a parameter == the count of lower txt using "o" as a parameter 
        # as a boolean value to the caller
        
    return lower_txt.count("o") == lower_txt.count("x")            
              
    

print(XO("ooxx"))       # ➞ True
print(XO("xooxx"))      # ➞ False 
print(XO("ooxXm"))      # ➞ True (Case insensitive)
print(XO("zpzpzpp"))    # ➞ True (Returns True if no x and o)
print(XO("zzoo"))       # ➞ False

