def sorting_bubbles_up(arr: list):
    """Sorts every two values on the list until the list is sorted Bubbles"""
    for i in range(len(arr)):
        sorted = True
        for j in range(0, len(arr) -1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        if sorted:
            break

arr = [1,9,-2,8,3,-7,4,6,5]
sorting_bubbles_up(arr)
print(arr)