from linked_list.linked_list import Node, LinkedList

def zip_list(Linked_List_1,Linked_List_2):
        """
        functions takes tow arguments which are lists and
        zip them and print them follow a templete

        Arg:

        Linked_List_1 : List of integers
        Linked_List_2 : List of integers

        Return:
        Zipped Linked List

        """
        ll_1 = Linked_List_1.head
        ll_2 = Linked_List_2.head

        if not ll_1 and not ll_2:
            return "there is no lists passed"
        elif not ll_1 or not ll_2  :
            return "one of lists is missing"

        temp =''
        while ll_1 and ll_2:
            if ll_2:
                temp = ll_1._next
                ll_1._next =ll_2
                ll_1=temp

            if ll_1 and ll_2:
                temp = ll_2._next
                ll_2._next=ll_1
                ll_2=temp
        result=f'head -> {str(Linked_List_1)}'
        return result





