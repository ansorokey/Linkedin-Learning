
## Introduction To Data Structures

### What is data?
Data is the information we can store and track.

### What is a data type?
A data type is the classification of data. A data type determines what the data is, and what we can do with it. Different data types are stored with different sizes of bits.

### What is a bit?
A bit is the smallest individual unit of computer memory storage: it's a 1 or a 0.

### What is a byte?
A byte is a group of 8 bits.

### What are the two types of number data type generally used in computer languages?
Whole (integer) and decimal (floating point).
JavaScript only has `number`.
Java has values like `short, int, long, double, float`. 
Python3 has `long`. 
The differences between these values determines the space (bits) used in memory to store a number. A 32-bit number can hold a larger value than an 8-bit number.

### What is the difference between signed and unsigned number values?
An unsigned number value can only be a positive number. This means that if it is a value that can store a 32-bit number, all 32 bits would go towards that entire number.
A signed number value is one where the first bit represents whether the number is positive or negative. This cuts the possible bits to use by the number down to 31, since one bit is saved for the sign. This means that the number can only be half as large as the unsigned version, but that half can go in the positive or negative direction.

### What is a boolean?
A boolean is a data type that only stores the value of true or false: 1 or 0. Similarly, they are stored with only a single bit: 1 or 0;
This can be used to represent a condition.

### What is a character?
A character is a single character in storage. This can be a letter or a symbol. Usually represented in languages wrapped in single quotes.

### What is a string?
A string is a sequence of characters in an specific order. In some languages, its a data type made of a data type. A string is not a primitive type since it can vary in size,

### What is a primitive type?
Primitive types are the basic data types. Specifically, they are the data types that are of a fixed size regardless of the contents or values. 1 is a smaller number than 123_456_789, but they are each 32-bit number values. The 32-bits are allocated regardless of the value. True is the same size as false, and so on.

### What are data structures?
*A data structure is a collection with a defined way of accessing and storing items.*
A data structure is data that is composed of other data. They are collections, and they organize data in different ways. A single primitive data type can hold only a single value. To store several values in memory, they would need to be grouped together. They make it easier to relate and keep track of data that would be isolated without them.

### What is a reference type?
A reference type is a data type that does not point directly to a value. Since primitive types are set data types with a set allocated size, they can be stored one after the other. a 32-bit number will never take up 33 bits.
A reference type like a string could be one character or ten, and so cannot fit in the same area in memory as primitive types.
Instead of pointing to the value, a reference type points to a pointer, which is a piece of data that points to an address in memory where the data structure is stored with variable space.
To demonstrate:
int a = 7;
a points to a location in memory which contains the value 7. 7 is located in that memory address.
String b = 'hello';
b points to a location in memory that contains an address. That address is the real location of the data.
If the address changes, the variable changes.

## Arrays

### What is an array?
An array is a collection that acts as a sequence of values. Arrays begin the first value indexed at 0. The index is used to refer to the position of the element is that sequence.

### How are array elements accessed?
We can access an element as a specific position by referring to it's index. 

### What is a multi-dimensional array?
A multi-dimensional array is an array of arrays. A collection of arrays. Also called a matrix.
These are typically used to represent grid like structures, with columns and rows.
The length of the parent array represents the column value (the number of rows) while the length of the subarray represents the row (number of columns).

### What is a jagged array?
A jagged array is a multi-dimensional array, but the length is the sub arrays can differ in size. This means that it is not a perfect square/rectangle shape. When iterating through, a master length cannot be used. The length of the subarray would need to be referenced.

### What is array resizing?
When an array is created, is is allocated space in memory. The size of the array can depend on how it is created. Depending on the language, they array can have additional elements slotted in beyond what it was given at creation. Or those slots can be removed to become smaller than when created.
A language that allows for an array to be resized has a dynamic array.
Not all languages handle array resizing the same. Depending on the language, resizing an array can involve creating an entirely new array, re populating it, and adding the new slots/elements. This can create performance issues at large enough sizes.

### How are arrays searched?
Since arrays are a sequence of elements stored at a sequenced index, arrays must be searched by looking over every individual index and seeing if the value ir holds matches the value being searched.
Worst case scenario, all elements have to be checked. This is a linear search, where the time to search is directly proportional to the number of elements/items searched.
An array search can be faster than linear search if the data contained is already sorted.

### How are arrays sorted?
Data types usually have an inherit order. Numbers are usually sorted by increasing or decreasing order. Strings are usually ordered alphabetically. If an item is a reference type/object, it may contain several values. A person object, for example, could have a name and an age. We would have to pick the value to sort by, which is our comparator.
Sorting can be very expensive in time and memory.

### What is Big O notation?
Big O notation is an assumption used to describe the performance or complexity of an algorithm/operation. Big O specifically refers to the longest possible case regardless of input.
In terms of time:
O(1) is constant time. This means we already know exactly where to look and locate an item by using an index. A collection with 1 or 1 million items will take the same amount of time. Accessing and updating an array is usually O(1).
If an array is full and we want to add an extra item at the end of it, the array would have to copy its contents to a new array and then add the new item. This makes insertion typically O(n) or linear. Searching is also linear, since we'd have to check every item if the item was not in the array.
Deleting an array could be fast, but worst case the item to be deleted is not in the array, so deletion is O(n).
Arrays are a good choice of data structure if you need only to sort once.

## Linked Lists

### What are linked lists?
A linked list is a linear data structure similar to an array, but each item is not next to each other in memory. Instead, each element in the list has a pointer that points to the memory location of the next item in the list. These items are referred to as a node. The fist node is the head, and all nodes in the list can be accessed from the head.
*A linked list is a series of connected nodes.*
Not all languages have an implementation of a linked list.

### How do we perform operations on a linked list?
We can do similar operations on a linked list that we can do on an array. A linked list is best at adding data to the front or ends of the list, since they can have pointers, and memory does not need to be adjusted, only pointed to.
Accessing items is more difficult in a linked list, since we can never access by index. It can only be searched, which makes deletion, search, and access linear.

### What is the difference between a single and doubly linked list?
A single linked list works with each node pointing only to the next node in the list. This means we can only travers the list in a single direction from any node.
A doubly linked list contains an additional pointer to refer to the node behind it. This way, we can traverse in either direction from any node. A doubly linked list will typically also store a tail in addition to a head, to refer to the last node for easier addition/deletion from either direction. 


### What are the pros and cons of a linked list?
Accessing, updating, searching and deleting an item in a linked list is O(n) since we have to jump from one node to another.
Inserting an item can either be O(1) or O(n) depending on if we want to add it to the front/end or if we want it somewhere in the list.

## Stacks

### What are stacks?
A stack is an ordered series of elements, but in an order where elements are accessed, added, and deleted from one side of a stack only.
This is a Last In, First Out (LIFO) order. To reach an item at the bottom of a stack, all other items must be removed first. Items are pushed onto a stack, and popped off. Viewing the next item is peeking without removing it.
Similar to a deck of cards.

### What are stacks good for?
Stacks work well for reversing something. In programming, the runtime or call stack keeps track of the functions running and variables currently accessible. When an error occurs, it can trace itself back to what caused that error further down the road.

### What are queues?
A queue is a sequence or ordered objects, but an order where elements are added from one direction, and removed from the other. Like a line in a store, the first person in line is served first, and the last person in line is served last. This follows a First in, First Out (FIFO) order.
Adding an item to a queue is enqueueing. Removing an item is dequeueing. Viewing the next item is peeking without removing it.

### What are queues good for?
Queues work well for keeping track of what events need to happen in an order. Things like printers need to print jobs in the order they are received.
### What is a priority queue?
A priority queue is like a normal queue, but each element has a priority associated with it. They are added in normal order, but they are dequeued in order of highest priority.

### What is a double ended queue?
A double ended queue - or dequek (deck) - is like a mix of a stack and a queue. Items can be added from either end, and removed from either end, but only from the ends.

### What are the pros and cons of stacks and queues?
Stacks excel in programs or situation where things need to be reversed. Think of strings. Characters are pushed onto a stack, and to reverse, we need only to pop them off. Also good for keeping track of states. They're also better for adding and removing from one side of a data structure. 
Stacks are poor for trying to access anything in the middle of a stack. Also poor at searching.
Queues excel at removing from one end and adding to the other. Poor at removing from the middle of structures, but okay at adding to the middle.


## Hashed-Based Data Structures

### What are associative arrays?
The index of an array is simply a number that represents the ordered position of an element. Some collections can store an element using a key, which is an index with a value.
An associative array is a collection of key-value pairs. in JavaScript, this would be an object. These key-value pairs do not have an explicit order, so they are not used for ordered data.

### What is hashing?
Hashing takes some sort of raw data and mixes it into a new, smaller form of data. The end result is a hash. The steps taken to turn something into a hash is the hashing function. The steps taken in the function can be highly complex, but is abstracted so that any input returns an output.
Hashing is not reversible. Things can only be hashed. A french fry cannot be turned back into a potato.
A simple example of a hashing function can be taking in a string 'hello', adding the bit values of the ascii characters together '00001111 10101010 11110000 11001100 01010101' and turning that number into a new number.
Hashing is important cyber security, which is why passwords are typically stored as hashed values. When any user logs into a website, the input should be immediately turned into a hash, and the hash is what is compared to the stored hashed password on the backend.
Encryption is similar to hashing, turning an input into an output, but encryption can be reversed, while hashing cannot.
### What is ASCII?
ASCII is the numerical representation of text characters. Every character on a keyboard is simply bits of 0s and 1s. The decimal value of those 0s and 1s is the the ascii value. t = 116. W = 119.

# What is a collision?
A collision is any two values that produce the same output.
When a value is hashed, the individual pieces that make up a value are turned into a hash result. A string '12345' can be hashed by adding every number together (1 + 2 + 3 +4 + 5) and the result 15 is the key. But this means that any order of the same characters will produce the same result. '54321' and '32415' would also hash to the key 15.

### What is a hash table?
A hash table is an implementation of an associative array. A hash table is composed of buckets, which are the places that a key-value pair can be stored. We will always store a key and a value, not just one or the other.
The number of buckets in a hash table may be limited to a certain number, so to spread values evenly, a modulo operation may be used.
The key is hashed into a smaller, easier to read value/number, and the value is stored at that index. That key is then modulated by the number of buckets in the table, and the value is stored in the matching bucket.
To demonstrate, say we had a hash table with 3 buckets. The number of possible modulo results can only be 0, 1, or 2. These are the three buckets.
To store the value '12345', it is hashed into the number 15. 15 % 3 is 0, so '12345' is stored in bucket 0. 
Python has dictionaries.
JavaScript does not have a hashtable, but can use objects

### What is separate chaining?
Separate chaining is storing a collection at an index that has a collision. Instead of the index pointing directly to the stored value, it points to the collection which the value is then stored in This decreases performance, since the collection at the bucket must be traversed.
The collection used is usually a linked list, since it only requires a pointer to the next value.
While an array could be used, this would mean that at the first instance of a hash, the value is stored. But on the second similar hash, that value would need to be replace with an array, and both values would need to be stored. This is functional, but slower than adding to the head of a linked list.

### What makes a reference type object equal?
For two objects to be considered equal, they would have to be the same object living in the same memory address. When storing an object in a hash table, or hashing an object in general, it is up to you to decide a comparator or how an object is hashed into storage

### When should we use hash tables?
Hash tables take up considerably more size in exchange for much faster searching, insertion, and deletion. Search, insertion, and deletion are all O(n) in a hash table when store in different buckets (no collisions) but become O(n) when a collision does occur and the value must be stored in a collection.
Hash tables have no means of being sorted.

## Trees and Graphs

### What are sets?
A set is a collection of unique items. A set is unordered, and contains no duplicates. A set is typically not used to retrieve data, but rather to track is a piece of data is contained within or not. A set is implemented similarly to a hash table, but instead of storing a key and its value, they key is the value, and the value is the key: storing only one piece of data.
A set checks whether an object has been stored or not by hashing the object. This means we would need the object on hand to even check if it is in the set.
This would be like asking if a stranger has seen your dog, and you hold up your missing dog to show an example. We already have access to the data we're looking for in a set, which is why sets are not used for retrieval of data. Only for the checking of membership or inclusion.

### What is a finite set?
A finite set is a set with predetermined elements. This means that elements won't be added or removed from the set. Primary colors, the letters of the alphabet, for example. In python, a finite set can be denoted with `frozenset([list of items])`

### What is an infinite set?
An infinite set is a set where the contained elements can change. Students in a class, or the planets of the solar system, for example.

### What is a tree?
A tree is a collection of nodes. Since a linked list is a collection of nodes, a linked list is also a tree, but more specified in its traversal and usage. A single node alone can be a tree as well. The node that a tree begins from is the root node. All other nodes can be access by traversing the root node.
A parent node is a node that points to child nodes. The root node of a tree has no parent node.
A child node is a node that is pointed to by a parent node.
Parent nodes can be the children of other nodes, and child nodes can be the parents of other nodes.
Child nodes that have the same parent node are called siblings.
A node with no children is a leaf node ( the end of a tree ).

### What is a binary tree?
A binary tree is a specialized tree where each node can only have two children, usually labelled left and right.

### What is a binary search tree?
A binary search tree is the implementation of a binary tree, but with an added constraint of order.
In a binary search tree, the value of left child is less than the value of the parent node, and the value of the right node is greater than the value of the parent node. This rule goes al the way down.
The nodes of a binary search tree usually represent key value pairs.
When adding or searching nodes in a binary search tree, the value is compared to the current node and put in its proper place (left or right).
Each time we head down the path of a child, we are effectively eliminating half of the searches needed to find a node. 

### What is an unbalanced tree?
An unbalanced tree occurs when there are more nodes on one side of a binary tree than the other. This means that additional steps would have to be performed when searching through that side of the tree than the other.

### What is a heap?
A heap is a data structure implemented as a binary tree. Where as a binary search tree has the constraint of order, a heap has the constraint where items are added top to bottom, left to right. This means one level is filled out at a time. Heaps are not used in many situations, but can be used in some.

### What is a min heap?
A min heap is a heap where the parent node is always the smallest value, and all children greater than the node's value.
When a value is added that is smaller than a child, the appropriate nodes are swapped going up the tree. The left and right order does not matter in this structure, as long as it is more than the parent.

### What is a max heap?
A max heap is a heap where the parent node is always the greatest value, and all children lesser than the node's value.
When a value is added that is greater than a child, the appropriate nodes are swapped going up the tree. The left and right order does not matter in this structure, as long as it is less than the parent.

### How does a priority queue get implemented?
A priority queue is often implemented with a min or max heap, since the top values will always be ordered.

### What are the pros and cons of a tree data structure?
Sets are best for checking if an item exists in a collection. They should only be used for checking membership.
Binary search trees excel at maintaining sorted order, insertion, deletion, and access. A balanced tree can be traversed in O(log(n)) time, since half the tree is removed from search with every movement.
Unbalanced trees can be O(n)
Rebalancing of trees may effect performance time.
Min/Max heaps can provide O(1) time when accessing the min/max of data, and O(log(n)) insertion, but searching and deleting are O(n) time