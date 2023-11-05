# Python code​​​​​​‌​‌​​‌‌​‌‌​​‌‌​​‌​​‌​​‌‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # Your code goes here.
    # We want to find out if a given string is a palindrome
    # A palindrome is the same sequence of characters forwards and reversed
    # A palindrome shuold ingore capitalization, spaces, and non-letter characters
    # This means that we only want to compare letters of the same case and reversed

    # Initial approach: since we're comparing a string against itself, lets make two strings: one with all ignored characters removed and normalized, and the same reversed. Then, we can compared them front to back.

    # Step 1: What are the characters that are allowed to be in a string?
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'

    # Step 2: trurn the given strig into a series of only valid characters
    str_forward = ''
    for c in teststr:
        if c.lower() in valid_chars:
            str_forward += c.lower()

    # Step 3: reverse the first string into another string
    str_back = str_forward[::-1]

    # step 4: compare if the strings are the same, return that result
    return str_forward == str_back

# TEST CASES
total = 0
test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.",
    "Race car!"]
for word in test_words:
    total += is_palindrome(word)

print(total) # Expecting 3
