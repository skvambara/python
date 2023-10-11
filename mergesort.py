import random


def merge(i_list, start, mid, end):
    leftlist = i_list[start:mid + 1]
    rightlist = i_list[mid + 1:end + 1]
    i = j = 0
    k = start
    while i < len(leftlist) and j < len(rightlist):
        if leftlist[i] >= rightlist[j]:
            i_list[k] = rightlist[j]
            j += 1
        else:
            i_list[k] = leftlist[i]
            i += 1
    k += 1

    while i < len(leftlist):
        i_list[k] = leftlist[i]
        k += 1
        i += 1

    while j < len(rightlist):
        i_list[k] = rightlist[j]
        j += 1
        k += 1


def helperfun(i_list, start, end):
    # base case
    if start < end:
        # internal worker node case
        mid = start + (end - start) // 2
        helperfun(i_list, start, mid)
        helperfun(i_list, mid+1, end)
        merge(i_list,start,mid, end)

def mergesort(i_list):
    helperfun(i_list, 0, len(i_list)-1)


inputlist = random.sample(range(10, 30), 10)
print("Original list:", inputlist)
mergesort(inputlist)
print("Sorted list:", inputlist)