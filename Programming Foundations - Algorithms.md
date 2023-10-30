
## Introduction

### What is an algorithm?
An algorithm is a process or a set of steps taken to achieve an outcome.
An algorithm can be complex is different ways:
Space complexity - the memory it requires
Time complexity - the time taken to run
Inputs and outputs - what the algorithm can take in and return
Classifications of an algorithm can include
serial, which runs sequentially
parallel, which breaks up into smaller pieces to run at the same time
exact, which produces a known predictable value
approximate, which might not be the same each time
deterministic, which executes each step with an exact decisions
non-deterministic, which runs with successive guesses with improving accuracy

### What are the most common algorithms?
Searching algorithms find specific data in a structure
Sorting algorithms plate the data in a structure in a particular order
Computational algorithms calculate data from a data set
Collection algorithms return information about data

### What is algorithm performance?
Big O notation is the worst case performance of an algorithm performs based on the size of the input given.
Data structures and algorithms can have different big O results.
Ordered by speed, we have:
Constant - O(1) - is the same speed regardless of input size.
Logarithmic - O(log(n)) - cuts the number of results to search through in half each step
Linear - O(n) - goes through every element 
Log-Linear - O(n log n) - used in heap and merge sort
Quadratic - O(n^2) - touch n elements n times

## Data Structures

### Why are data structures used with algorithms?
Data structures organize data in a way that allow it to be processed for a specific purpose.
The most commonly used structures include arrays, linked lists, stacks and queues, trees, and hash tables

### Arrays
An array is a collection of elements where the position of each element is identified by its index.
An element in an array can be accessed in memory using a mathematical equation. Since the first index of every array is 0, any other index is a modification of 0. 
Some array operation speeds are:
Calculate item index - O(1)
inserting or deleting at beginning - O(n)
inserting or deleting at middle - O(n)
inserting or deleting at end - O(1)

### Linked Lists
A list list is a collection of nodes that points to the next element in the list, like a chain. The first item is the head, the last item is the tail, and points to nothing.
Linked Lists can be singly linked (points to the next neighbor) or doubly linked (points to next and prev neighbor)
Linked lists elements can easily add and remove items, and memory does not need to contiguous.
Some linked list operations speeds are:
insertion and deletion at head - O(1)
insertion and deletion in middle - O(n)

### Stacks and Queues
A stack is a collection that support pushing and popping. They are first In last Out. Pushing and popping from a stack is a constant time operation. Stacks are usually used in expression statements and mathematical notation, backtracking, going back on a web browser.
Queues are collections that support enqueueing and dequeueing. They are first in first out. They are usually used for order processing, message processing

### Hash maps
A hashmap is a collection of items where the value stored is indexed by a hashed key value. one of the benefits of a hash table is the ability to map a unique key to a unique value. They are also typically much faster than other structures, at the cost of more memory and size. For very small values, an array may be better, and the values are not ordered in any particular way.

## Recursion

### What is recursion?
Recursion is when a function calls itself from within its code.
A recursive function must have a breaking condition that causes it to stop and return. Otherwise, it will run forever.
Each time the function runs, the previous data values are set aside on the call stack.

## Sorting

### Why do we sort data?
Sorting data can make it easier to understand data. It also makes it easier to work with data. Most languages have built in sorting.

### What is the bubble sort?
The bubble sort is the most basic implementation of a sort. This sort method goes one element at a time and swaps positions until that item reaches its destination.
This is hen repeated until every item is sorted, which makes it quadratic in time complexity - O(n^2).
When implementing, keep in mind that we can decrease the number of time we need to swap by one since the last element should be the min, max already.

### What is the merge sort?
The merge sort is known as the divide and conquer sort. It breaks a data set down into smaller pieces and uses recursion to sort the smaller sets of data.
Typically performs in linear logarithmic time - O(n log n)
An array of unsorted numbers is repeatedly broken down into smaller arrays until broken down into smaller arrays from tyhe mid point (left and right) until they are 1 or 0 length arrays. These are by definition sorted (the only value is in the correct place)
Two sorted arrays are then passed back up and merged together in a zipper like fashion into a larger array.
This process continues all the way up
The merge portion of this sort takes two sorted arrays and merges them into one single array.

## What is the quicksort?
The quicksort is another divide and conquer algorithm that uses recursion, typically performs faster or similarly to merge sort.
Unlike merge sort, which creates a new array, quick sort can be done in place.
The quick sort works on a pivot point.
We can pick any pivot position, so let's pick the first value.
Every other value in the array is then going to be a number either greater than or lower than the pivot point.
we take two pointers to represent smaller and greater numbers
The lower index continues to move up until a number is found thats greater than pivot
We do the same with the greater.
If the lower and greater values find a value that should be swapped, swap them and continue
stop doing this when the indexes of the pointers cross each other.
After they cross, swap the pivot with the former upper limit index
now every left is smaller, and everything right is bigger

## Searching Data

### How do we search data in an unordered list?
In an unordered list, there is no guarantee where something might be. The only way to search for one matching item would be an iterative O(n) search where each element is checked for a match.

### How do we search data in an ordered list?
When data is already sorted, search becomes much more efficient. Ordered data allows for the use of a binary search.

### What is a binary search?
A binary search is a search performed on ordered data. In a binary search, we have three pointers: a lower pointer, a mid pointer, and an upper pointer. if the mid point is the value we want, we return it. If not, then we now have two sides of the data: numbers greater and numbers lower. based on the value we're looking for, we can then pick the half we need, change the pointers, and repeat the process. This runs in logarithmic time.
The search ends when the pointers cross over each other.

```py
def binarySearch(nums, val):

    lower = 0

    upper = len(nums) - 1

  

    while lower <= upper:

        mid = (lower + upper) // 2

        if nums[mid] == val:

            return mid

        elif val < nums[mid]:

            upper = mid - 1

        elif val > nums[mid]:

            lower = mid + 1

  

    return None
```

### How do we determine if a list is already sorted?
The only way to prove that a list is in order is to perform an iteration and check each function and compare it to the previous element

## Other Algorithms

### What can we use a hash table for?
Since the keys of a hash table are unique, a hash table can store items. If the key exists, it will be overridden and not duplicated. At the end, we can extract the keys as a set of unique items.
It is also very good for counting instances of unique items. Rather than overwriting a value, we can set a count when first encountered, and increment the corresponding value when encountered again

### How can we use recursion on lists?
When we use a recursive function, we need to ensure that something is changing with each call. With a list, we can modify an index that is passed to all calls, or we can pass in a modified version of the original list.
Keep in mind that recursion is not always the most efficient or necessary action