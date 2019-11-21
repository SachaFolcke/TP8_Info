"""TP noté de Sacha FOLCKE"""
### Imports
import random
import time
import sys
###
def random_array_gen(num):
    """Generate an array containing n random integers between 0 and 100"""
    array = []
    for _ in range(num):
        array.append(random.randint(0, num))
    return array

### Tri à bulle
def swap(array, ind1, ind2):
    """Swaps two values in an array and returns it"""
    old = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = old
    return array

def bubble_sort(array):
    """Performs a bubble sort on an array and returns it"""
    for _ in array:
        for cpt in range(len(array) - 1):
            if array[cpt] > array[cpt+1]:
                array = swap(array, cpt, cpt+1)
    return array

### Tri rapide
def quick_split(array, first, last):
    """Find all numbers smaller than the pivot and put them at the beginning of the array"""
    pivot = array[first]
    swap(array, first, last)
    inf = first
    for cpt in range(first, last):
        if array[cpt] < pivot:
            swap(array, cpt, inf)
            inf += 1
    swap(array, last, inf)
    return inf

def quick_sort(array, first, last):
    """Performs a quick sort on an array and returns it"""
    if first < last:
        pivot = quick_split(array, first, last)
        quick_sort(array, first, pivot-1)
        quick_sort(array, pivot+1, last)
    return array

### Tri fusion
def fusion_sort(array):
    """Splits the arrays in two for the sort"""
    if len(array) < 2:
        return array
    return fusion(fusion_sort(array[:(len(array)//2)]), fusion_sort(array[(len(array)//2):]))

def fusion(array_a, array_b):
    """Merge sorted arrays"""
    if not array_a:
        return array_b
    if not array_b:
        return array_a
    if array_a[0] <= array_b[0]:
        return [array_a[0]] + fusion(array_a[1:], array_b)
    return [array_b[0]] + fusion(array_a, array_b[1:])

# Time Benchmark
def benchmark(sizes_array, num):
    """Who is the best sorting algorithm ??
    Generates a random array of 'size' integers long, then let each algorithm sort
    the exact same array. Outputs the results in multiple files. Repeat 'num' times."""
    sys.setrecursionlimit(500000)
    for size in sizes_array:
        file_bu = open('./sorts/bubble_' + str(size), 'a')
        file_qu = open('./sorts/quick_' + str(size), 'a')
        file_fu = open('./sorts/fusion_' + str(size), 'a')
        bubbles = []
        quicks = []
        fusions = []
        for _ in range(num):
            init_array = random_array_gen(size)
            array = init_array.copy()
            time1 = time.time()
            bubble_sort(array)
            time2 = time.time()
            total_time = str(time2 - time1)
            bubbles.append(time2 - time1)
            print("Bubble sort " + str(size) + " : " + total_time + " s")
            file_bu.write(total_time + "\n")
            #####
            array = init_array.copy()
            time1 = time.time()
            quick_sort(array, 0, len(array)-1)
            time2 = time.time()
            total_time = str(time2 - time1)
            quicks.append(time2 - time1)
            print("Quick sort " + str(size) + " : " + total_time + " s")
            file_qu.write(total_time + "\n")
            #####
            array = init_array.copy()
            time1 = time.time()
            fusion_sort(array)
            time2 = time.time()
            total_time = str(time2 - time1)
            fusions.append(time2 - time1)
            print("Fusion sort " + str(size) + " : " + total_time + " s")
            file_fu.write(total_time + "\n")

        file_bu.write("Moyenne : "+ str(sum(bubbles)/len(bubbles)))
        file_qu.write("Moyenne : "+ str(sum(quicks)/len(quicks)))
        file_fu.write("Moyenne : "+ str(sum(fusions)/len(fusions)))


if __name__ == "__main__":
    #print(bubble_sort(random_array_gen(20)))
    #print(quick_sort(random_array_gen(10), 0, 9))
    #print(fusion_sort(random_array_gen(20)))
    benchmark([10, 100, 1000, 10000, 100000], 100)
