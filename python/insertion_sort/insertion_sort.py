def insertion_sort(list):

    sorted=list
    for ind in range(1,len(sorted)):
        k=ind-1
        temp=sorted[ind]
        print(ind,k,temp,sorted)
        while k>=0 and temp <list[k]:
            list[k+1] = list[k]
            k-=1
        list[k+1]=temp
    return sorted
