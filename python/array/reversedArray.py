array = [1,2]


def reversedArray(array: int):
    if(len(array) != 0):
        res = array[::-1]
        return res
    else:
        return print("The Array Is empty")


if __name__ == "__main__":
    print("***************************")
    print("Algorithm 1")
    reversedArray(array)
    print("***************************")
