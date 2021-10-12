# Binary Search in an Array

<!-- Description of the challenge -->

It's a python function project takes in 2 parameters: a sorted array and the search key.

return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process

<!-- Embedded whiteboard image -->

![array_binary_search](/python/array_binary_search/array_binary_search.jpg)

## Approach & Efficiency

<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->

    the while loop will be termneated when the lower index become higher index
    and this will casue number of operation depending on the location of the target element and the list length so it's linear O(n) notation.
