from trees.tree import Queue,kArrayTree,Node

def fizz_buzz_tree(tree):
    """
    Fizz Buzz Function

    Arg : Tree with depthfirst style
    Return : New array with fizz_buzz mutation for the tree values

    """
    try:
        new_tree=[]
        for element in tree:
            if element %3 == 0 and element % 5==0:
                new_tree+=["FizzBuzz"]
            elif element %3 == 0:
                new_tree+=["Fizz"]
            elif element % 5==0:
                new_tree+=["Buzz"]
            else:
                new_tree += [str(element)]
        print(f"Original Tree : {tree}")
        print(f"Modified Tree : {new_tree}")
        return new_tree
    except :
        print("Your Input Is not a tree")
        return None
