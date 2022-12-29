# NoneType data type

# Empty value
# Many programming languages ​​(Java, C++, C#, JavaScript, etc.) have the null keyword that can be assigned to variables. The concept behind the null keyword is that it gives a variable a neutral or "null" behavior.

# In Python, the word null is changed to None because null doesn't sound very friendly, and None refers specifically to the required functionality - it's nothing, and has no behavior.

# Literal None
# The None literal in Python allows you to represent a null variable, that is, a variable that does not contain any value. Essentially, None is a special constant that means empty. More specifically, None is an object of the special data type NoneType.

# The following program code:
# var = None
# print(type(var))          - <class 'NoneType'>

# We can assign the None value to any variable, but we cannot create another NoneType object ourselves.

# All variables assigned the value None refer to the same object of type NoneType. Creating your own instances of type NoneType is not allowed. Objects that exist in a single instance are called singletons.


# Check for None
# To test the value of a variable for None, we use either the is operator or the == equality operator.

# The following program code:
# var = None
# if var is None:       # use the is operator
# print('None')
# else:
# print('Not None')
# will output: None

# The following program code:
# var = None
# if var == None:       # use the == operator
# print('None')
# else:
# print('Not None')
# will output: None

# NOTE: To compare a variable with None, always use the is operator. For built-in types, the behavior of is and == is exactly the same, but there can be problems with user-defined types, since Python has the ability to override comparison operators in user-defined types.


# Comparing None with other data types
# Comparing None with any object other than None results in False.

# The following program code:
# print(None==None)
# will output:
# True

# The following program code:
# print(None == 17)                 - False
# print(None == 3.14)               - False
# print(None==True)                 - False
# print(None == [1, 2, 3])          - False
# print(None == 'Beegeek')          - False

# It is important to understand that the following program code:

# print(None == 0)          - False
# print(None==False)        - False
# print(None == '')         - False

# You can only compare None with other data types for equality.

# The following program code:
# print(None > 0)
# print(None <= False)

# results in an error:
# TypeError: '>' not supported between instances of 'NoneType' and 'int' ('bool')


# NOTE:
# Note that non-returning functions actually return None in Python.

# def print_message() :
#     print('I am Timur,')
#     print('king matan. ')

# We can call the print_message() function like this:
# print_message()

# or like this:
# res = print_message()
# The res variable holds the value None.
