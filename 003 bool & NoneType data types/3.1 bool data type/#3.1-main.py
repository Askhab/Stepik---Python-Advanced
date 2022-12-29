# bool data type

# Data types in Python
# Text Type:    	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type: 	dict
# Set Types:    	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type:    	NoneType

# Boolean type
# Boolean data type (Boolean type, Boolean) is a primitive data type in computer science that takes two possible values, sometimes called true (True) and false (False). It is present in the vast majority of programming languages as an independent entity or is implemented through a numerical data type. Some programming languages accept 11 as true and 00 as false.
#
# The type name Boolean was given in honor of the English mathematician and logician George Boole, who, among other things, dealt with mathematical logic in the middle of the 19th century.

# Boolean data type in Python
# The logical values True (true) and False (false) represent the bool data type. This type has only two possible values and two corresponding literals: True and False.
#
# We used the boolean data type extensively when we worked with checkboxes:
#
# flag = False

# or when using an if-else conditional statement:
#
# a = 100
# b = 17
#
# if b > a:
# print('b is greater than a')
# else:
# print('b is not greater than a')

# The result of the logical expression b > a is a Boolean value, False in this example, because the value in variable b is less than the value in variable a.
#
# Boolean expressions can be used in more than just a conditional statement.

# The following program code:
#
# print(17 > 7)     - True
# print(17 == 7)    - False
# print(17 < 7)     - False


# Logical operators in Python
# To create arbitrarily complex logical expressions (conditions), we use three logical operations:

# and (and);
# or (or);
# not (not).

# Boolean operations use operands with True and False values and return a result also with Boolean values. The operators (and, or, not) defined on objects of type bool are known as logical operators and have well-known definitions:

# a and b evaluates to True if both operands are True and False if at least one of them is False;
# a or b gives False if both operands are False and True if at least one of them is True;
# not a is True if a is False and False if a is True.

# The following program code:

# a=True
# b=False

# print('a and b is', a and b)  - a and b is False
# print('a or b is', a or b)    - a or b is True
# print('not a is', not a)      - not a is False

# NOTE: The not operator has a higher precedence than the and operator, which in turn has a higher precedence than the or operator.


# Boolean values as numbers
# Boolean values in Python can be treated as numbers. True value corresponds to the number 11, while False value corresponds to 00. Thus, we can compare boolean values with numbers:

# The following program code:

# print(True == 1)      - True
# print(False == 0)     - True

# We can also apply arithmetic operations to booleans.
# The following program code:

# print(True + True + True - False)     - 3
# print(True + (False / True))          - 1.0

# The ability to treat Boolean expressions as numbers is not used very often in practice. However, there is one trick that may be useful. Because True is 11 and False is 00, adding booleans together is a quick way to count the number of True values. This can be useful when you want to count the number of elements that satisfy a condition.

# The following program code:
# numbers = [1, 2, 3, 4, 5, 8, 10, 12, 15, 17]
# res = 0
#
# for num in numbers:
#     res += (num % 2 == 0)
# print(res)
# will display the number of even elements in the numbers list, i.e. the number 5.


# NOTES:
# Note 1: Instead of redundant code:
# if flag == True:
#
# programmers usually write code:
# if flag:

# Likewise, instead of code:
# if flag == False:
#
# programmers usually write code:
# if not flag:

# Note 2: The and and or operators are lazy:
# when evaluating the logical expression x and y, if x == False, then the result of the entire expression x and y will be False, so y is not evaluated;
# when evaluating the boolean expression x or y, if x == True, then the result of the entire expression x or y will be True, and y is not evaluated.

# Note 3: The mathematical theory of Boolean logic defines that no other operators other than not, and and or are needed. All other statements on the two inputs can be specified in terms of these three statements. All statements on three or more inputs can be specified in terms of operators on two inputs.

# In fact, even having a pair of or and and is redundant. The and operator can be defined in terms of not and or, and the or operator can be defined in terms of not and and. However, and and or are so useful that all programming languages have both.


# bool() Function
# To cast other data types to boolean, there is a bool() function that works according to the following conventions:
# strings: empty string — false (False), non-empty string — true (True);
# numbers: zero number - false (False), non-zero number (including less than zero) - true (True);
# lists: an empty list is false (False), a non-empty list is true (True).

# The following program code:
# print(bool('Beegeek'))                - True
# print(bool(17))                       - True
# print(bool(['apple', 'cherry']))      - True
# print(bool())                         - False
# print(bool(''))                       - False
# print(bool(0))                        - False
# print(bool([]))                       - False

# Note: If the bool() function is called with no arguments, it will return False.


# Functions that return a boolean value
# We can create functions that return boolean values (True or False). This practice is very helpful. Let's write an is_even() function that takes a single number and returns True if the passed number is even and False otherwise:

# def is_even(num):
#     return num % 2 == 0

# The following program code:
# print(is_even(8))     - True
# print(is_even(7))     - False


# isinstance() Function
# Python has a built-in isinstance() function to check if an object type matches a data type.
#
# The following program code:
# print(isinstance(3, int))                 - True
# print(isinstance(3.5, float))             - True
# print(isinstance('Beegeek', str))         - True
# print(isinstance([1, 2, 3], list))        - True
# print(isinstance(True, bool))             - True

# The following program code:
# print(isinstance(3.5, int))               - False
# print(isinstance('Beegeek', float))       - False


# type() Function
# Python has a built-in type() function that allows you to get the type of the object specified as an argument.

# The following program code:
# print(type(3))                - <class 'int'>
# print(type(3.5))              - <class 'float'>
# print(type('Beegeek'))        - <class 'str'>
# print(type([1, 2, 3]))        - <class 'list'>
# print(type(True))             - <class 'bool'>

# NOTE: Note that typechecking usually uses the isinstance() function instead of the type() function because it takes the type hierarchy (OOP) into account.
