nums = [14,7,9,49,6,32,29,90,32,43]

largest = second = nums[0]

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num < largest:
        second = num

print(second)