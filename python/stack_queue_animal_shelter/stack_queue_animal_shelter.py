from stack_and_queue.stack_and_queue import Queue

class AnimalShelter:
    def __init__(self):
        self.dogs= Queue()
        self.cats= Queue()

    def add_animal(self,name,type):
        """
        The Add Animal Method for adding animal using enquee method of Queue Class
        Arg   :
            name : string value refere to the animal name
            type : string value refere to the animal type

        Return: messege if the passed type of cat is not dog or cat
        """
        animal={
            "name":name,
            "type":type
        }
        if type=="cat":
            self.cats.enqueue(animal)
        elif type=="dog":
            self.dogs.enqueue(animal)
        else:
            print("Invalid animal type entered. Animals must be cat or dog.")
    def adopt_animal(self,pref):
        """
        The Adopt Method for removing animal form shelter using enquee method
        from Queue class directly from front
        Arg   :
            pref: user prefere value to be passed and select either dog or cat
        Return: None if the passed pref is not dog or cat
        """
        if pref == 'dog':
            return self.dogs.dequeue()
        elif pref =='cat':
            return self.cats.dequeue()
        else:
            return None

if __name__ =="__main__":

    instance=AnimalShelter()
    instance.add_animal("suzy","cat")
    instance.add_animal("sobhi","dog")
    instance.adopt_animal("dog")
    print(instance.adopt_animal("cat"))

