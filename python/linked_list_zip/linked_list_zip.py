import sys
sys.path.append('/media/jehadabuawwad/EA20F40B20F3DC8F/data-structures-and-algorithms/python')
from linked_list.linked_list import Node, LinkedList

def zip_list(Linked_List_1,Linked_List_2):

        ll_1=Linked_List_1.export_as_List()
        ll_2=Linked_List_2.export_as_List()

        zipped_Object=zip(ll_1,ll_2)
        lista=list(zipped_Object)
        
        output = ""
        for item in lista:
            output +=  "{ " + f"{item[0]}" + " }" + " -> " + "{ " + f"{item[1]}" + " }" + " -> "
        with_head= "head" + " -> " + output
        with_tail="X"
        result= with_head + with_tail
        if len(result)>9:
            return result
        else :
         return "You have entered empty lists and non empty lists are allowed only"


if __name__=="__main__":

    Linked_List_1=LinkedList()
    Linked_List_2=LinkedList()

    Linked_List_1.add(1)
    Linked_List_1.add(3)
    Linked_List_1.add(2)
    Linked_List_2.add(5)
    Linked_List_2.add(9)
    Linked_List_2.add(4)


    print(zip_list(Linked_List_1,Linked_List_2))
