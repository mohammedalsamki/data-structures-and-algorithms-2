def insertion_sort(list):

    sorted=list
    for ind,itm in enumerate(sorted):
        k=ind-1
        temp=itm

        while k>=0 and temp <list[k]:
            list[k+1] = list[k]
            k-=1
        list[k+1]=temp
    return sorted


