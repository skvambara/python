import random

def insertsort(i_list):
    for i in range(len(i_list)):
        temp = i_list[i]
        index = i-1
        while index >= 0 and i_list[index] > temp:
            i_list[index+1] = i_list[index]
            index -= 1
        i_list[index+1] = temp
    return i_list



# inputlist = random.sample(range(10, 30), 10)
inputlist = [5, 8, 3, 9, 4, 1, 7]
print(inputlist)
sorted_list = insertsort(inputlist.copy())
print(sorted_list)

