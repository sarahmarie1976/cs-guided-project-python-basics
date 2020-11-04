"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

use the built in sort to sort our list and return it to the caller

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
# def sort_by_length(lst):
#     # run the built in ".sort" method on the list
#     lst.sort(key = len)  # will assort in ascending order

#     # return the list to the caller
#     return lst


def sort_by_length(lst):
    
    # return the list from the built in method sorted() using the key of len to the caller
    return sorted(lst, key = len)   

print(sort_by_length(["a", "ccc", "ddd", "bb"]))                    # ➞ ["a", "bb", "ccc", "dddd"]
print(sort_by_length(["apple", "pie", "shortcake"]))                # ➞ ["pie", "apple", "shortcake"]
print(sort_by_length(["may", "april", "september", "august"]))      # ➞ ["may", "april", "august", "september"]
print(sort_by_length([]))                                           # ➞ []