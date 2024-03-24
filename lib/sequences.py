#!/usr/bin/env python3

# A dynamic sequence of values that allows duplicates
fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# An immutable, ordered sequence of months
month_tuple = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
)

# A simple pattern of numbers
even_numbers_up_to_100 = range(0, 101, 2)

# A grammatical sentence
sentence_string = "Strings are immutable sequences of Unicode code points."

def print_fibonacci(length):
    fibonacci = []
    if length:
        fibonacci.append(0)
    if length >= 2:
        fibonacci.append(1)
        for i in range(2, length):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

    print(fibonacci)

s = [4, 6, 3, 9, 3, 5, 1, 2]
1 in s
# => True
s + s
# => [4, 6, 3, 9, 3, 5, 1, 2, 4, 6, 3, 9, 3, 5, 1, 2]
s * 2
# => [4, 6, 3, 9, 3, 5, 1, 2, 4, 6, 3, 9, 3, 5, 1, 2]
s[1]
# => 6
s[-1]
# => 2
s[2:5]
# => [3, 9, 3]
s[2:5:2]
# => [3, 3]
len(s)
# =>  8
min(s)
# => 1
max(s)
# => 9
s.index(3)
# => 2
s.count(9)
# => 1f

# if we sort numbers, they will be sorted in ascending order
my_list = [3, 6, 4, 2, 1, 5]
my_list.sort()
print(my_list)
# [1, 2, 3, 4, 5, 6]

# If we sort strings, they will be sorted in alphanumeric order
my_list = ['Cabbage', 'Apple', 'Banana', 'Potato']
my_list.sort()
print(my_list)
#['Apple', 'Banana', 'Cabbage', 'Potato']