def summinnum(nums):
    min1, min2, *rest_value = nums
    # min2 = nums[1]

    if min1 > min2:
        min1, min2 = min2, min1

    # for i in range(0, len(nums)):
    for element in rest_value:
        if element < min1:
            min2 = min1 
            min1 = element
        elif element < min2:
            min2 = element

    return min1, min2, min1 + min2


nums = [19, 5, 42, 2, 77]

fun = summinnum(nums)
print(fun)


                
  