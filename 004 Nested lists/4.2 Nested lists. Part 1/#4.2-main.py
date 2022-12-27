# NESTED LISTS

# Introduction
# As we already know, a list is an ordered sequence of elements numbered from 00. List elements can be any data type - numbers, strings, booleans, etc. For example,
#
# numbers = [10, 3]
# constants = [3.1415, 2.71828, 1.1415]
# countries = ['Russia', 'Armenia', 'Argentina']
# flags = [True, False]

# The numbers list has 2 elements, and each of them is an integer:
# numbers[0] == 10;
# numbers[1] == 3.

# The list of constants consists of 3 elements, each of which is a real number:
# constants[0] == 3.1415;
# constants[1] == 2.71828;
# constants[2] == 1.1415.

# The list of countries consists of 3 elements, each of which is a string:
# countries[0] == 'Russia';
# countries[1] == 'Armenia';
# countries[2] == 'Argentina'.

# The flags list has 2 elements, and each of them is a boolean value:
# flags[0] == True;
# flags[1] == False.

# We also said that the elements of a list do not have to be of the same data type. The list can contain values of different data types:
# info = ['Timur', 1992, 72.5]

# The info list contains a string value, an integer, and a float:
# info[0] == 'Timur';
# info[1] == 1992;
# info[2] == 72.5.

# NOTE: Typically, the elements of a list contain data of the same type, and in practice it is rarely necessary to create lists containing elements of different data types.


# Nested lists.
# Creation of nested list
# It turns out that the elements of lists can be other lists, and in practice this construction turns out to be very useful. Such lists are called nested lists.

# Working with nested lists is fundamentally no different from working with lists, for example, of numbers or strings. To create a nested list, we also list the items separated by commas in square brackets:
# my_list = [[0], [1, 2], [3, 4, 5]]

# The variable my_list refers to a list of other lists (with nested lists).

# NOTE: Since the nesting depth of my_list is two, this list is usually called a two-dimensional list. In practice, as a rule, we work with two-dimensional lists, less often with three-dimensional ones.

# Consider the program code:
# my_list = [[0], [1, 2], [3, 4, 5]]
#
# print(my_list)                - [[0], [1, 2], [3, 4, 5]]
# print(my_list[0])             - [0]
# print(my_list[1])             - [1, 2]
# print(my_list[2])             - [3, 4, 5]
# print(len(my_list))           - 3


# Indexing
# When working with one-dimensional lists, we used indexing, that is, referring to a specific element by its index. Nested lists can be indexed similarly:
# my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik']]
#
# print(my_list[0])         - Python
# print(my_list[1])         - [10, 20, 30]
# print(my_list[2])         - ['Beegeek', 'Stepik']

# Since the elements of my_list are string and lists, they can also be indexed.
# Consider the program code:
# my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik!']]
#
# print(my_list[0][2])              - t
# print(my_list[1][1])              - 20
# print(my_list[2][-1])             - Stepik!
# print(my_list[2][-1][-1])         - !

# An attempt to access a list element at a non-existent index:
# print(my_list[3]) # list my_list has indices from 0 to 2
# will throw an error:
#
# IndexError: index out of range


# len(), max(), min() Functions
# Consider the program code:
# my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]
#
# print(len(my_list))           - 5

# Note that the built-in function len() returns the number of elements (the number 55) of the list my_list, not the total number of elements in all lists (the number 99).

# If we want to count the total number of elements in the nested list my_list, we can use a for loop in conjunction with the len() function:
# total = 0
# my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]
#
# for li in my_list:
#     total += len(li)
#
# print(total)              - 9

# The variable li sequentially takes all the values of the elements of the list my_list, that is, it is a list itself, so we can call the len() function with the argument li passed.


# The min() and max() functions can also work with lists. If several lists are passed to these functions, then one of the passed lists is returned in its entirety. In this case, the comparison occurs element by element: first, the first elements of the lists are compared. If they are not equal, then the min() function will return the list whose first element is less, max() - vice versa. If the first elements are equal, then the second elements will be compared, and so on.
#
# Consider the program code:
# list1 = [1, 7, 12, 0, 9, 100]
# list2 = [1, 7, 90]
# list3 = [1, 10]
#
# print(min(list1, list2, list3))       - [1, 7, 12, 0, 9, 100]
# print(max(list1, list2, list3))       - [1, 10]


# The min() and max() functions can also be used when working with nested lists. Consider the program code:
# list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
# list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]
#
# print(min(list1))         - [1, 7, 12, 0, 9, 100]
# print(max(list1))         - [1, 10]
# print(min(list2))         - ["a"]
# print(max(list2))         - ["d", "p", "q"]

# Please note that the elements of nested lists in this situation must be comparable.
#
# So the following code:
# my_list = [[1, 7, 12, 0, 9, 100], ['a', 'b']]
#
# print(min(my_list))
# print(max(my_list))

# will result in an error:
# TypeError: '<' not supported between instances of 'str' and 'int'


# NOTES:
# Note 1. Regardless of the nesting of lists, we need to remember all list methods whenever possible:
#
# 1 - the append() method adds a new element to the end of the list.
# 2 - the extend() method extends one list with another list.
# 3 - the insert() method inserts a value into the list at the given position.
# 4 - the index() method returns the index of the first element whose value equals the value passed to the method.
# 5 - the remove() method removes the first element whose value equals the value passed to the method.
# 6 - the pop() method removes the element at the specified index and returns it.
# 7 - the count() method returns the number of elements in the list whose values are equal to the value passed to the method.
# 8 - the reverse() method inverts the order of the values in the list, i.e. reverses it.
# 9 - the copy() method creates a shallow copy of the list.
# 10 - the clear() method removes all elements from the list.
# 11 - the del operator allows you to delete elements of a list at a specific index.

# Note 2. String methods that work with lists:
# 1 - the split() method splits a string into words using a sequence of whitespace characters, a tab character (\t), or a newline character (\n) as a delimiter.
# 2 - the join() method collects a string from the elements of the list, using the string to which the method is applied as a delimiter.

# Note 3: Python does not restrict us to levels of nesting: the elements of a list can be lists, their elements can be other lists, whose elements can in turn be other lists...
