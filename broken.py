from typing import List

def quick_sort(numbers:List):
   quick_sort_helper( numbers, 0, len(numbers)-1)

def quick_sort_helper(numbers:List, first:int, last:int)->None:
   if first<last:

       splitpoint = partition(numbers, first, last)

       quick_sort_helper(numbers, first, splitpoint-1)
       quick_sort_helper(numbers, splitpoint+1, last)


def partition(numbers:int, first:int, last:int)->int:
   pivotvalue = numbers[first]

   leftmark =  first 
   rightmark = last

   done = False
   while not done:
    while leftmark <= rightmark and numbers[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

    while numbers[rightmark] >= pivotvalue and rightmark >= leftmark:
        rightmark = rightmark -1

    if rightmark <= leftmark :
        done = True
    else:
        numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark] # swap
    # undo the swap
    numbers[first] , numbers[rightmark] = numbers[rightmark], numbers[first]

   return rightmark

numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before Sort: {}".format(numbers))
quick_sort(numbers)
print("After Sort: {}".format(numbers))
