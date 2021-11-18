# Hashtables

Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

## Challenge

Implementation of Hash Tables

## Approach & Efficiency

Hash maps take advantage of an array’s O(1) read access. Instead of adding elements to an array from beginning to end, a hash map uses a “hash function” to place each item at a precise index location, based off it’s key.

**Read Acsess O(1)**

## Features

* [] Implement a Hashtable Class with the following methods:

    - [] add
        - [] Arguments: key, value
        - [] Returns: nothing
        - [] This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
    - [] get
        - [] Arguments: key
        - [] Returns: Value associated with that key in the table
    - [] contains
        - [] Arguments: key
        - [] Returns: Boolean, indicating if the key exists in the table already.
    - [] hash
        - [] Arguments: key
        - [] Returns: Index in the collection for that key

## Test Requirements

* [] Adding a key/value to your hashtable results in the value being in the data *  structure
* [] Retrieving based on a key returns the value stored* []
* [] Successfully returns null for a key that does not exist in the hashtable* []
* [] Successfully handle a collision within the hashtable* []
* [] Successfully retrieve a value from a bucket within the hashtable that has a * collision
* [] Successfully hash a key to an in-range value* []
* [] # White Board


## White Board
![Hash]()
