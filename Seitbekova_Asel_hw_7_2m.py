def binary_search(list_1,key):
    First = 0
    Last = len(list_1) - 1
    while First <= Last:
        midle = (First + Last)//2
        if list_1[midle] == key:
            return f' The element is at index: {midle}'
        elif list_1[midle] > key:
            Last = midle - 1
        elif list_1[midle] < key:
            First = midle + 1
    return f'Your element was not found'

x = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


print(x)
print(binary_search(x,16))


def linear_search(arr,search_item):
    low = 0
    search_result = False

    while low < len(arr) and not search_result:
        if arr[low] == search_item:
            search_result = True
        else:
            low += 1

    return search_result

lst = [34,2,34,7,87,45,12,43]
value = int(input('Enter element:'))
result = linear_search(lst,value)
if result:
    print('Item found!')
else:
    print('There is no such element!!')