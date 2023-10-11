# selection sort - Brute force
# Scan through the list and identify the least weighted element and swap with the current element
import random

# Create a list with 10 random elements between 10 - 30


def selectionsort(i_list):
    for i in range(len(i_list)):
        minindex = i #c1 *n
        for j in range(i+1, len(i_list)):
            if i_list[j] < i_list[minindex]:    #c2 * n * n
                minindex = j                    #c3 * n * n
        i_list[minindex], i_list[i] = i_list[i], i_list[minindex]       #c4 * n * n
    return i_list

"""
S = 1+2+3 ... +n-1
s = n-1 + n-2 + n-3 + 1
2s = n + n + n +.. + n ---- n-1 times = n(n-1)
T(n) = an^2 + bn + c
drop the lower order terms
to make the analysis system independent ignore the constant factors
T(n) ~ Theta(n^2)
"""

inputlist = random.sample(range(10, 30), 10)
print(inputlist)
print(selectionsort(inputlist))
