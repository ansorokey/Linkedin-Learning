## Python Language Features

### Styling
The PEP 8 guide is the standard syntax for python. While exacts and specifics can be viewed [here](https://peps.python.org/pep-0008/), the most essential recommended style for writing python code is:
- Import statements should be at the very top, each with their own line
- Indent code with spaces instead of tabs
- use four spaces for each indentation level
-  limit the length of any line to 79 characters, 72 for comments and doc strings
- separate functions and classes by two blank lines
- separate methods in a class with one line
- no whitespace around function calls, indexed, or keyword arguments

These conventions have no effect on the performance f the code, but do make it easier for you and other developers to read. here is an example of what a piece of python may look like
```py
# imports go on their own lines
import sys
import os


# two blank lines separate classes from other functions
class MyClass():
    def __init__(self):
        self.prop1 = "my class"

    # within classes, one blank line separates methods
    def method1(self, arg1):
        pass


def main():
    # Long comments, like this one that flow across several lines, are
    # limited to 72 characters instead of 79 for lines of code.
    cls1 = MyClass()
    cls1.prop1 = "hello world"


if __name__ == "__main__":
    main()
```


### Truth Values
Generally, anything in python is evaluated to true unless it has a `bool` method that returns false, or a `len` method that returns 0.
The two built in values that can represent false are `False` and `None`. 
Any numerical values that represent 0 are also false. 
Empty sequences/collections (lists, tuples, sets, strings) are false.
A range of 0 is false.

Custom objects are by default true. But we can override and give them functions that return true.

The basic boolean operations are written out as `and, or, not`. The `and` operand short circuits, meaning it will only check the second value if the first is true. The `or` will only check the second value if the first is false.

```py
x=[] -> False

y={}
print(bool(y)) -> False

# in JavaScript, these would evaluate to true
```

### Strings Vs Bytes
A string in python is a sequence of unicode characters.
A byte is a sequence of raw 8-bit values.
Bytes and strings do not go together
 ```py
 b = bytes([0x41, 0x42, 0x43, 0x44]) # represents the ascii values of 4 characters
print(b) # -> b'ABCD'

s = "I am a string"
print(s) # -> I am a string

# While they both represent characters, they cannot be concatenated as is
# Need to use the decode method
s2 = b.decode('utf-8')

print(s+s2) # -> I am a stringABCD

# Or we could go the other way, and turn a string into a sequence of bytes
b2 = s.encode('utf-8')
print(b+b2) # -> b'ABCDI am a string'

b3 = s.encode('utf-32')
print(b3) # -> b'\xff\xfe\x00\x00I\x00\x00\x00 \x00\x00\x00a\x00\x00\x00m\x00\x00\x00 \x00\x00\x00a\x00\x00\x00 \x00\x00\x00s\x00\x00\x00t\x00\x00\x00r\x00\x00\x00i\x00\x00\x00n\x00\x00\x00g\x00\x00\x00'
```


### Template Strings
Formatting strings is one of the most common things done in python. Template strings are one of the formats and methods available to use built in to python.

```py
# Standard string formatting
animal = 'cat'
furniture = 'chair'
# The variable order determines the outcome
str1 = "The {0} jumped over the {1}".format(animal, furniture)
# -> The cat jumped over the chair
str2 = "The {1} jumped over the {0}".format(animal, furniture)
# -> The chair jumped over the cat

print(str1)
print(str2)
```

```py
# Template class
from string import Template

str_templ = Template("${name} chased squirrels at the ${place}")
str1 = str_templ.substitute(name="Luna", place="park")
print(str1)

# Since the substition uses keyword arguments, we can pass in a dictionary instead

data = {
    "name": "Luna",
    "place":  "park"
}

str2 = str_templ.substitute(data)
print(str2)
```

## Built-In Functions
### Utilities
There are approx. 70 built in functions for python (this does not count class methods). Try to use built in functions whenever possible to improve performance with native code
Here are some:
```py
# any and all return a boolean value based on the condition on a collection
list1 = [0, 1, 2, 3, 4, 5, 6]
print(any(list1)) # -> at least 1 value is true
print(all(list1)) # -> not all values are true

# min and max return the minimum and maximum values
# sum retuns the sum
list2 = [2, 4, 6, 8]
print(min(list2))
print(max(list2))
print(sum([min(list2), max(list2)]))
```


### Iterators
Iterating over collections is an essential part of programming. An iterator is an iterable object from a sequence.

```py
days = ['m', 't', 'w', 't', 'f', 's', 's']
day_iter = iter(days);
print(next(day_iter))
print(next(day_iter))
print(next(day_iter))
```

An iterator becomes most useful when working with functions to return the next iteration (think RPG dialog text)

```py
new_dialog = open('dialog.txt', '+w')
for i in range(5):
    new_dialog.write('I am line ' + str(i) + '\n')
new_dialog.close()

with open('dialog.txt', 'r') as text:
    for line in iter(text.readline, ''):
        print(line)
```

An enumerator is another object that returns an iterator with an index and a value in tuples
```py
days = ['m', 't', 'w', 't', 'f', 's', 's']
for i, d in enumerate(days, start=1):
    print(i, d)
# -> 
1 m
2 t
3 w
4 t
5 f
6 s
7 s
```

The zip function takes any number of functions and combines then into a single collection. A zip function will terminate when the shortest collection is finished.
```py
gen1 = ['bulb', 'squirt', 'char']
gen2 = ['chiq', 'toto', 'cynd']
gen3 = ['tree', 'mud', 'torch']
gen4 = ['turt', 'pip', 'chim']

for p in zip(gen1, gen2, gen3, gen4):
    print(p)
# -> 
('bulb', 'chiq', 'tree', 'turt')
('squirt', 'toto', 'mud', 'pip')
('char', 'cynd', 'torch', 'chim')
```


### Transforms
Python is an excellent language for modifying sequences and data into other forms

The filter function creates an iterator and filters out values that fail a boolean condition
```py
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chars = 'aBcdEfgHIjkLMNopQ'

def filter_lower(c):
    return c == c.lower()

def filter_even(x):
    return x % 2 == 0

evens = list(filter(filter_even, nums))
print(evens)

lowers = list(filter(filter_lower, chars))
print(lowers)
```

The map function returns each element modified by the given function
```py
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def square(x):
    return x*x

squares = list(map(square, nums))
print(squares) # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

sorted creates a sorted list of a given sequence
```py
scores = [13, 59, 10, 90, 99, 67, 84, 76, 100]
def to_grade(x):
    if x >= 90:
        return 'A'
    elif x < 90 and x >= 80:
        return 'B'
    elif x < 80 and x >= 70:
        return 'C'
    else:
        return 'F'

grades = list(map(to_grade, scores))
print(grades) # -> ['F', 'F', 'F', 'A', 'A', 'F', 'B', 'C', 'A']
grades = sorted(grades)
print(grades) # -> ['A', 'A', 'A', 'B', 'C', 'F', 'F', 'F', 'F']
```

### Itertools
The itertools module is part of the standard library that comes with python language.

```py
import itertools

# the cycle method iterates in a loop endlessly
seq1 = ['Dante', 'Vergil', 'Nero']
iter1 = itertools.cycle(seq1)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

# the count creates a counter with a starting and step value
count1 = itertools.count()
print(next(count1))
print(next(count1))
print(next(count1))

# the accumulate aggregates values together,
# defaults to addition but the function can be changed
vls = [10, 20, 30, 40, 50, 60, 70, 80, 90]
acc = itertools.accumulate(vls, max)
print(next(acc))
print(next(acc))
print(next(acc))


# the chain connects sequences together
abcs = 'abc'
one_two_threes = '123'
chain = itertools.chain(abcs, one_two_threes)
print(list(chain))


# dropwhile and takewhile will return values until a condition is met
# takewhile will return values until it fails a condition
# dropwhile will ignore values until it passes a test
# passing or failing a test after doesnt matter
vls = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def bigger_than_40(x):
    return x < 40

take = list(itertools.takewhile(bigger_than_40, vls))
print(take)
drop = list(itertools.dropwhile(bigger_than_40, vls))
print(drop)
```


## Advanced Python Functions

### Function Documentation Strings
Python provides an easy way to view the built in documentation for native functions. This can run on function, classes, and packages.
```py
import collections

print(map.__doc__)
print(collections.__doc__)
```

We can also write our own. Write a brief description of the available arguments, parameters, default values, return values, etc within triple double quotes
```py
def my_func():
	"""
My_func(arg1, arg2) -> prints given arguments

Parameters:
arg1: The first argument
arg2: The second argument
	"""
print(my_func.__doc__)
```

Some best practices include:
- Always use triple quotes, even if only one line
- The first line should summarize functionality
- For a module, list important classes, functions, and exceptions
- For classes, list important methods, enums
- For functions, list parameters on seperate lines
- list a return value only if there is one
- if the function raises exceptions, list those
### Variable Argument Lists
A function that can take in any number of arguments can be done with a variable argument list. When defining a function with a variable argument list, define a name and prepend it with an asterisk. If using any positional or keyword, arguments, they must come before the variable arguments

The variable argument parameter becomes an iterable list in the function definition

```py
def my_func(*args):
    return sum(args)

print(my_func(1, 2, 3, 4, 5))
```

### Lambda functions
A lambda function is a small usually one line function. Like a callback function, they can be passed as arguments where a function is needed. They are good for use in places where defining a separate function might be unnecessary

They are defined as: `lambda params: expression`. The return value is the implicit result of the expression (the return keyword is not needed)
```py
def cTOf(temp):
    return (temp * 9/5) + 32

def fTOc(temp):
    return (temp - 32) * 5/9

f_temps = [90, 80, 70, 32]
c_temps = [36, 20, 0]

# the map function takes a function and an iteable to create a new list
print(list(map(cTOf, c_temps)))

# instead of defining a whole function for one purpose, we can use a lambd ain it's place
print(list(map(lambda t: (t - 32) * 5/9, f_temps)))
```


### Keyword only arguments

Python functions can take positional arguments as well as keyword arguments
When calling a function, arguments can be defined by position or keyword.
We can also force a function to provide a keyword if we want. To do so, separate positional arguments from keyword arguments with a single asterisk in the parameter list.
```py
def no_key(arg1, upper=False):
	print(arg1)

def need_key(arg1, *, upper=False):
	print(arg1)

print(no_key('hello', True)) # -> prints hello
print(need_key('hello', True)) 
# -> throws exception because a parameter is in the keyword's place, but isn't named
print(need_key('hello', upper=True)) # -> prints hello
```


## Advanced Collections
Python has some basic built in collection types: 
- list [a, b, c] - mutable
- tuple (a, b, c) - immutable,
- set {a, b, c} - mutable,
- dictionary {"a": 1, "b": 2, "c", 3} mutable

There are also advanced collections that can be accessed by importing `collections`. These include:
- namedTuple - tuple with named fields
- OrderedDict, defaultDict - dictionaries with special properties
- Counter - counts distinct values
- deque - double ended list

### namedtuple
if we wanted to reference the coordinated of a point, we could use a tuple, and access each point with `p[0]` and `p[1]` respectively. `(6, 8)`. But this isn't very descriptive, and doesn't really communicate what we're looking at.

A namedtuple allows us to name the positions in a tuple.
```py
import collections

# creating a tuple type called Point with names X and Y
Point = collections.namedtuple('Point_Name', 'x y')
# Now we can use it like a constructor
p1 = Point(10, 20)
p2 = Point(5, 10)

print(p1) # -> Point_Name(x=10, y=20)
print(p2) # -> Point_Name(x=5, y=10)
#  Now we can access tuple values by name instead of index
print(p1.x, p1.y)

# the _replace method allows us to reconstruct a tuple with a different value while keeping the other
p1 = p1._replace(x=11)
print(p1) # -> Point_Name(x=11, y=20)
```


### DefaultDicts
the defaultdict is a good way to reduce some of the often used conditions and code used with regular dictionaries.
Counting instances is one of the most common uses of a dictionary
if the item has not been counted yet, we add it to the dictionary and count it at 1, otherwise we increase the count by 1
Encountering the item for the first time will only ever happen once for nay item, so that step can be removed from the code with a defaultDict
A defaultdict will give EVERY key a default value, so it might not be the best choice for instances where we need to track missing keys
```py
from collections import defaultdict

# defaults to a value of 0 for any key not encountered before
# calls the int function, which defaults to 0
# fruit_counter = defaultdict(int)
# just needs to be any callable function, even a lambda
fruit_counter = defaultdict(lambda: 10)

fruits = ['apple', 'banana', 'orange', 'apple']

for f in fruits:
    fruit_counter[f] += 1

for k, v in fruit_counter.items():
    print(k, v)
```


### Counters
One of the uses of dictionaries is to count the instances of keys
The counter has good options for working with lists
```py
from collections import Counter

class_one = ['naruto', 'sasuke', 'sakura', 'kakashi', 'naruto', 'naruto', 'naruto', 'inner demon']
class_two = ['itadori', 'megumi', 'nobora', 'gojo', 'gojo', 'inner demon']

c1 = Counter(class_one)
c2 = Counter(class_two)

# since a counter is a dictionary, we can access a count by referring to the key
print(c1['naruto'])

# we can find the total number of items
print(sum(c1.values()))

# we can combine values
c1.update(class_two)
print(sum(c1.values()))

# we can print the x most common values
print(c1.most_common(3))

# we can also subtract classes from each other
c1.subtract(class_two)
print(c1.most_common(3))

#  We can see what's common between the two
print(c1 & c2)
```


### OrderedDict
A regular dictionary does not keep track of order. The ordereddict will do that.

```py
from collections import OrderedDict

teams = [
('Royals', (18, 12)), ('Rockets', (24, 6)), ('Cardinals', (20, 10)), ('Dragons', (22, 8))
]

# sort teams by number of wins
sortedteams = sorted(teams, key=lambda t: t[1][0], reverse=True)

# create an ordered dictionary of the teams
dictteams = OrderedDict(sortedteams)

print(dictteams) # -> ([('Rockets', (24, 6)), ('Dragons', (22, 8)), ('Cardinals', (20, 10)), ('Royals', (18, 12))])

# we can use popitem to remove the top item
name, scores = dictteams.popitem(False)
print(name, scores)

# Equality in ordered dicts checks to see if the values are the same and in the same order
a = OrderedDict({"a": 1, "b": 2})
b = OrderedDict({"b": 2, "a": 1})
c = OrderedDict({"b": 2, "a": 1})
print(a == b) # False - different orders
print(b == c) # True - same order same values
# A plain dictionary's order would not matter when comparing to an OrderedDict
```


### Deque (deck)

Like a hybrid between a stack and a queue. Is memory efficient, and allows data to be appended and popped from either end. Can be initialized as empty or from an iterable.
Add with append or appendleft to add to right or left.
Remove with pop or popleft
The rotate function will shift items left or right
```py
from collections import deque
import string

# All the lowercase letters
d = deque(string.ascii_lowercase)
print(len(d))

# for c in d:
#     # replace newline with a comma
#     print(c.upper(), end=",")

# Can pop from either side
d.pop()
d.popleft()

#Can add from either side
d.append(1)
d.appendleft(2)

for c in d:
    # replace newline with a comma
    print(c, end=",")

d.rotate(10)

print('\n')
for c in d:
    # replace newline with a comma
    print(c, end=",")

```

## Advanced Python Classes
Python allows us to define how classes are effected by operations, expressions, comparisons, etc
### Defining Enumerations
Enums are human readable values, or a better way to read constant values for classes.
Enums should not have duplicate names, but they can have duplicate values
```py
from enum import Enum, unique, auto

@unique # applying this decorator forces enum values to be unique
class Fruits(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    FUJI = 1 # duplicate values are okay
    PEAR = auto() # adds the next value in sequence

print(Fruits.APPLE)
print(type(Fruits.APPLE))
print(repr(Fruits.APPLE))

# Enums have a name and a value
print(Fruits.APPLE.name, Fruits.APPLE.value)
```

### Class String Functions
We can convert different types of things into a string format, like an int to a string
We can do the same thing with a class
Python has 4 main ways to do this
	`object.__str__(self)`
	`object.__repr__(self)`
	`object.__format__(self, format_spec)`
	`object.__bytes__(self)`

```py
class Person():
    def __init__(self):
        self.fname = 'Anton'
        self.lname ='Sorokey'
        self.age = 26

    def __repr__(self):
        return "<Person Class - fname: {0}, lname: {1}, age: {2}>".format(self.fname, self.lname, self.age)

    def __str__(self):
        return "{0} {1} is {2}".format(self.fname, self.lname, self.age)

    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))

me = Person()

print(repr(me))
print(str(me))
print(bytes(me))
print("{0}".format(me))
```