lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]

def selection_sort(lst):
    i = 0
    length = len(lst)
    while i < length - 1:
        count = i + 1
        min = i
        while count < length:
            if lst[count] < lst[min]:
                min = count 
            count += 1
        lst[i], lst[min] = lst[min], lst[i]
        i += 1
    return lst 

def max(lst):
    sorted_lst = selection_sort(lst)
    return sorted_lst[-1]

def min(lst):
    sorted_lst = selection_sort(lst)
    return sorted_lst[0]
    
print(selection_sort(lst))
print(max(lst))
print(min(lst))