# Рекурсия

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
list=[]
for e in range(1, 10):
    list.append(fib(e))
print (list)                            # 1 1 2 3 5 8 13 21 34


def quicksort(array): # Быстрая сортировка с помощью рекурсии
    if len(array) <=1:
        return  array
    else:
        pivot = array[0]
    less=[i for i in array[1:] if i <= pivot]
    greater=[i for i in array[1:] if i > pivot]
    return quicksort(less)+[pivot]+quicksort(greater)
print(quicksort([15, 7, 9, 34, 56, 2, 1, 6, 13]))

def merge_sort(nums): # Сортировка слиянием с помощью рекурсии
    if len(nums)>1:
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1
list1=[1,5,3,7,4,9,11,15,14,14,2]
merge_sort(list1)
print(list1)
