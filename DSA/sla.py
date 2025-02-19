def num(nums, target):
    left, right = 0, len(nums) - 1
    steps = 0
    while left < right:
        mid = int((left + right) / 2)
        if nums[mid] < target:
            left = mid + 1
            steps += 1
        else:
            right = mid
            steps += 1
    print(steps)
    return left

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
num(nums, target)