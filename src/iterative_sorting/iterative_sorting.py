# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # smallest_index = cur_index

        # TO-DO: find next smallest element
        for j in range(cur_index + 1, len(arr)):
            smallest_index = j
            if arr[smallest_index] < arr[cur_index]:
                # TO-DO: swap
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]


    return arr

print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 66, 45]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    def new_swap(val1, val2):
        arr[val1], arr[val2] = arr[val2], arr[val1]

    arr_len = len(arr)
    status = True
    i = -1

    while status:
        status = False
        i = i + 1
        for val1 in range(1, arr_len - i):
            if arr[val1 - 1] > arr[val1]:
                new_swap(val1 - 1, val1)
                status = True

    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7, 66, 45]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr