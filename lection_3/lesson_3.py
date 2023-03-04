# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# def sum_str(*args):  # * Передача неограниченого кол-ва аргументов.
#     res = ''
#     for i in args:
#         res += i
#     return i

# def max1(a, b):
#     if a > b:
#         return a
#     return b

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
    
# print(quick_sort([1, 3, 212, 321, 22, 12, 13, 15,65 , 320]))

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums [:mid]
        right = nums [mid:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
            
list_1 = [1, 3, 212, 321, 22, 12, 13, 15,65 , 320]
merge_sort(list_1)
print(list_1)