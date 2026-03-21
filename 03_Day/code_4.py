# Tuples => immutable => ()

# t = (1, 2, 3, 4, 5)
t1 = (1, 2, 3, 4, 5, "modi", 3.14)

t2 = ("anshu",)     # jb ek value print krna hota hai
print(t2)
print(type(t2))

# print(t)
# print(type(t))


t = (1, 2, 3, 4, 5, 2, 2)
# sum = 0

# for val in t:
#     sum += val

# print(f"Sum is {sum}")

print(t.index(2))
print(t.count(2))