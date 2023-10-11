import random

def bubblesort(i_list):
    for i in range(len(i_list)):
        for j in range(len(i_list)-1, i, -1):
            if i_list[j] < i_list[j-1]:
                i_list[j], i_list[j-1] = i_list[j-1], i_list[j]
    return i_list


inputlist = random.sample(range(10, 30), 10)
print(inputlist)
sorted_list = bubblesort(inputlist.copy())
print(sorted_list)