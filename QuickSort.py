def quickSort(arr, left, right):
    i, j = left, right
    pivo = arr[int((left+right)/2)]

    while (i<=j):
        while (arr[i] < pivo and i < right):
            i = i+1
        while (arr[j] > pivo and j > left):
            j = j-1
        
        if i <= j:
            y = arr[i]
            arr[i] = arr[j]
            arr[j] = y
            i = i+1
            j = j-1
    
    if j > left:
        quickSort(arr, left, j)
    if i < right:
        quickSort(arr, i, right)
    
    return arr