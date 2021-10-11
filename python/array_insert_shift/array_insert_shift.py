"""
 Args:
    array : Empty or Array with values being passed and value added to it
    n : The value being added

 Returns:
    array : new Array with updated values

 Raises :
    if the type of n parameter is string it will raise that the user should enter integer
    as a messege and get out of program

"""


def insertShiftArray(array, n):
    finished = False
    if type(n) == str:
        print("Please enter a postive integer")
    else:
        array += [n]
        # This part commented for testing reasons after the test pass you can uncomment it
        # while finished is False:
        #     state = input(
        #         f"Your new Array is {array} with value added to it Do you want to add more values.. Enter yes or no please  \n> ")
        #     if state == 'no':
        #         finished = True
        #     elif state == 'yes':
        #         value = int(input(
        #             f"Add your value.. ? \n> "))
        #         array += [value]
        #         finished = False
        #     print("Array", array)
        return array


if __name__ == "__main__":

    insertShiftArray([1, 2], 5)
