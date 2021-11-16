def quick_sort(left, right, arr):
    if (left < right):
        p = partition(left, right, arr)
        quick_sort(left, p - 1, arr)
        quick_sort(p + 1, right, arr)
    return arr

def partition(left, right, arr):
    pivot = arr[right]
    low=left-1
    for i in range(left,right):
        if arr[i]<=pivot:
            low+=1
            swap(arr,i,low)
    swap(arr,right,low+1)
    return low+1
def swap(arr,i,low,):
    temp=arr[i]
    arr[i]=arr[low]
    arr[low]=temp

