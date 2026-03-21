# Lists
# mutable(particular index ki value change kr skte hai) seq of values

marks = [99, 80, 45, 65, 35]
marks2 = [99, 80, 45, 65, 35, "modi", 5.2]

# marks[2] = 100
# print(marks)
# print(marks2)

# print(marks[4])
# print(len(marks))

# Methods
nums = [1, 2, 3]

# nums.append(5)
# nums.insert(1, 7)
# nums.sort()
# nums.sort(reverse=True)     # decreasing order
# print(nums)

# nums.reverse()
# print(nums)


# nums3 = [14, 55, 40, 80, 50]
# for val in nums3:
#     print(val)


nums4 = [50, 45, 18, 25, 97]

x = 180
idx = 0

for val in nums4:
    if(val == x):
        print(f"{x} found at index={idx}")
        break
    idx += 1