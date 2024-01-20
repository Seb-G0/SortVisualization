from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Data import Array
class Sorts:
    def __init__(self, arr):
        self.arr = arr
        self.visualized_arrays = [arr.copy()]

    def bubbleSort(self):
        tempArray = self.arr.copy()
        n = len(tempArray)
        for i in range(0, n - 1):
            swap = False
            for j in range(0, n - 1 - i):
                if tempArray[j] > tempArray[j + 1]:
                    swap = True
                    tempArray[j], tempArray[j + 1] = tempArray[j + 1], tempArray[j]
                    self.visualized_arrays.append(tempArray.copy())
            if not swap:
                break

    def insertionSort(self):
        tempArray = self.arr.copy()
        for i in range(1, len(tempArray)):
            k = i
            while k > 0 and tempArray[k] < tempArray[k - 1]:
                tempArray[k], tempArray[k - 1] = tempArray[k - 1], tempArray[k]
                self.visualized_arrays.append(tempArray.copy())
                k -= 1
        return tempArray

    def selectionSort(self):
        tempArray = self.arr.copy()
        for i in range(len(tempArray)):
            minswap = i
            for j in range(i, len(tempArray)):
                if tempArray[j] < tempArray[minswap]:
                    minswap = j
            tempArray[minswap], tempArray[i] = tempArray[i], tempArray[minswap]
            self.visualized_arrays.append(tempArray.copy())
        return tempArray

    def bidirectionalSelectionSort(self):
        arr = self.arr.copy()
        n = len(arr)
        for i in range(n // 2):
            min_swap = i
            max_swap = i
            for j in range(i, n - i):
                if arr[j] < arr[min_swap]:
                    min_swap = j
                if arr[j] > arr[max_swap]:
                    max_swap = j
            if max_swap == i:
                if min_swap == n - i - 1:
                    arr[min_swap], arr[max_swap] = arr[max_swap], arr[min_swap]
                arr[n - i - 1], arr[max_swap] = arr[max_swap], arr[n - i - 1]
                arr[i], arr[min_swap] = arr[min_swap], arr[i]
            elif max_swap == n - i - 1:
                arr[i], arr[min_swap] = arr[min_swap], arr[i]
            else:
                arr[i], arr[min_swap] = arr[min_swap], arr[i]
                arr[n - i - 1], arr[max_swap] = arr[max_swap], arr[n - i - 1]
            self.visualized_arrays.append(arr.copy())
        return arr

    def shellSort(self):
        tempArray = self.arr.copy()
        gap = len(tempArray) // 2
        while (gap > 0):
            for i in range(0, len(tempArray), gap):
                k = i
                while k > 0 and tempArray[k] < tempArray[k - gap]:
                    tempArray[k], tempArray[k - gap] = tempArray[k - gap], tempArray[k]
                    self.visualized_arrays.append(tempArray.copy())
                    k -= 1
            gap //= 2
        return tempArray

    def shakerSort(self):
        arr = self.arr.copy()
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        while (swapped == True):

            swapped = False

            for i in range(start, end):
                if (arr[i] > arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    self.visualized_arrays.append(arr.copy())

            if (swapped == False):
                break

            swapped = False

            end = end - 1

            for i in range(end - 1, start - 1, -1):
                if (arr[i] > arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    self.visualized_arrays.append(arr.copy())

            start = start + 1

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        self.visualized_arrays.append(array.copy())
        return i + 1

    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)

    def clear(self):
        self.visualized_arrays = []

def update(frame):
    ax.clear()
    current_list = lists_to_animate[frame]
    ax.bar(np.arange(len(current_list)), current_list, color='blue')
    ax.set_xticks(np.arange(len(current_list)))
    ax.set_xticklabels([str(x) for x in current_list])
    ax.set_title(f'Frame {frame + 1}/{len(lists_to_animate)}')


def mergeSort(arr):
    n = len(arr)
    size = 1

    iterations = []

    while size < n:
        left = 0

        while left < n - 1:
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            merged = merge(arr, left, mid, right)
            arr[left:left + len(merged)] = merged

            left += 2 * size
            iterations.append(arr.copy())

        size *= 2

    return iterations

def merge(arr, left, mid, right):
    merged = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1

    while i <= mid:
        merged.append(arr[i])
        i += 1

    while j <= right:
        merged.append(arr[j])
        j += 1

    return merged



#BUBBLE SORT
arr = Array()
sort_algorithm = Sorts(arr)
sort_algorithm.bubbleSort()
lists_to_animate = sort_algorithm.visualized_arrays
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(lists_to_animate), repeat=False, interval=10)
plt.suptitle("BubbleSort", fontsize=16)
plt.show()

#SELECTION SORT
arr = Array()
sort_algorithm = Sorts(arr)
sort_algorithm.selectionSort()
lists_to_animate = sort_algorithm.visualized_arrays
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(lists_to_animate), repeat=False, interval=50)
plt.suptitle("SelectionSort", fontsize=16)
plt.show()

#INSERTION SORT
sort_algorithm.clear()
sort_algorithm.insertionSort()
lists_to_animate = sort_algorithm.visualized_arrays
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(lists_to_animate), repeat=False, interval=10)
plt.suptitle("Insertion Sort", fontsize=16)
plt.show()

#SHELL SORT
sort_algorithm.clear()
sort_algorithm.shellSort()
lists_to_animate = sort_algorithm.visualized_arrays
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(lists_to_animate), repeat=False, interval=10)
plt.suptitle("Shell Sort", fontsize=16)
plt.show()

#MERGE SORT
sort_algorithm.clear()
array = arr.copy()
lists_to_animate = mergeSort(array)
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(lists_to_animate), repeat=False, interval=200)
plt.suptitle("Merge Sort", fontsize=16)
plt.show()

#BIDIRECTIONAL
sort_algorithm.clear()
sort_algorithm.bidirectionalSelectionSort()
lists_to_animate = sort_algorithm.visualized_arrays
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(lists_to_animate), repeat=False, interval=100)
plt.suptitle("Bidirectional Selection Sort", fontsize=16)
plt.show()

#SHAKER
sort_algorithm.clear()
sort_algorithm.shakerSort()
lists_to_animate = sort_algorithm.visualized_arrays
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(lists_to_animate), repeat=False, interval=10)
plt.suptitle("Shaker sort", fontsize=16)
plt.show()

#QUICKSORT
sort_algorithm.clear()
array = sort_algorithm.arr.copy()
sort_algorithm.quickSort(array, 0, len(array) - 1)
lists_to_animate = sort_algorithm.visualized_arrays
fig, ax = plt.subplots()
animation = FuncAnimation(fig, update, frames=len(lists_to_animate), repeat=False, interval=10)
plt.suptitle("Quick Sort", fontsize=16)
plt.show()










