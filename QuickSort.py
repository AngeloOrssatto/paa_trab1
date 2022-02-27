# # Python program for implementation of Quicksort Sort

# # This function takes last element as pivot, places
# # the pivot element at its correct position in sorted
# # array, and places all smaller (smaller than pivot)
# # to left of pivot and all greater elements to right
# # of pivot

import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(6000)
# print(sys.getrecursionlimit())

# def partition(arr, low, high):
#     i = (low-1)		 # index of smaller element
#     pivot = arr[high]	 # pivot

#     for j in range(low, high):

# 		# If current element is smaller than or
# 		# equal to pivot
#         if arr[j] <= pivot:

# 			# increment index of smaller element
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1)

# # The main function that implements QuickSort
# # arr[] --> Array to be sorted,
# # low --> Starting index,
# # high --> Ending index

# # Function to do Quick sort


# def quickSort(arr, low, high):
#     if len(arr) == 1:
#         return arr

#     if low < high:

#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr, low, high)
#         # print('pi', pi)
#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)


# # Driver code to test above
# # arr = [10, 7, 8, 9, 1, 5]
# # n = len(arr)
# # quickSort(arr, 0, n-1)
# # print("Sorted array is:")
# # for i in range(n):
# # 	print("%d" % arr[i])

# # This code is contributed by Mohit Kumra
# #This code in improved by https://github.com/anushkrishnav

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

# alist = [54,26,93,17,77,31,44,55,20]
# quickSort(alist)
# print(alist)
