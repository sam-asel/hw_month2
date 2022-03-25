def linear_search(arr,search_item):
    new = 0
    search_result = False

    while new < len(arr) and not search_result:
        if arr[new] == search_item:
            search_result = True
        else:
            new += 1

    return search_result

lst = [34,2,34,7,87,45,12,43]
value = int(input('Enter element:'))
result = linear_search(lst,value)
if result:
    print('Item found!')
else:
    print('There is no such element!!')