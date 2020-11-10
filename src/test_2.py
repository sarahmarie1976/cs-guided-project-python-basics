"""
Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False
Notes:

Any string that contains spaces or is empty should return False.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] boolean

[Python 3] Syntax Tips


"""


def csAlphanumericRestriction(input_str):
    
    # if just letters 
        # check for just letters
    if input_str.isalpha():
        return True
    # if just numbers
        # check for just numbers
    if input_str.isdigit():
        return True

    # else string has both letters and numbers return false
    else:
        return False
    
print(csAlphanumericRestriction("Bold"))  
print(csAlphanumericRestriction("123454321"))  
print(csAlphanumericRestriction("H3LL0"))