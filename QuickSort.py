def quickSort(arr, left, right):
    i, j = left, right # Initialize left and right counters
    pivot = arr[int((left+right)/2)] # Middle element chosed as pivot

    while (i<=j):
        # Increase the left counter until it reaches the right counter
        while (arr[i] < pivot and i < right):
            i = i+1
        # Decrease the right counter until it reaches the left counter
        while (arr[j] > pivot and j > left):
            j = j-1
        
        if i <= j: # Swap and contiue
            y = arr[i]
            arr[i] = arr[j]
            arr[j] = y
            i = i+1
            j = j-1
    
    # Recursive call if there more slices to sort 
    if j > left:
        quickSort(arr, left, j)
    if i < right:
        quickSort(arr, i, right)
    
    return arr