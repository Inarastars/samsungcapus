def search_insert_position(nums, x):
    for i in range(len(nums)):
        if x <= nums[i]:
            return i
    return len(nums)
nums = [10, 20, 30, 40, 50, 60, 70, 80]
x = int(input("input a number to insert: "))
pos = search_insert_position(nums, x)
print(f"{x} should be inserted at position {pos}")
nums.insert(pos, x)
print(nums)