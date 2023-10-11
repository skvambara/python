import random

def partition(i_list):
    low = 0
    high = len(i_list)
    pivot = i_list[low]
    i = low
    j = high
    while i <= j:





inputlist = random.sample(range(10, 30), 10)
print("Original list:", inputlist)
quicksort(inputlist)
print("Sorted list:", inputlist)